#include <aspect/material_model/melt_simple.h>
#include <aspect/simulator_access.h>

namespace aspect
{
  namespace MaterialModel
  {
    using namespace dealii;

    template <int dim>
    class DensityGradientApproximation : public MaterialModel::MeltSimple<dim>
    {
      public:

        virtual void evaluate(const MaterialModel::MaterialModelInputs<dim> &in,
                              MaterialModel::MaterialModelOutputs<dim> &out) const;

        /**
         * Declare the parameters this class takes through input files.
         */
        static
        void
        declare_parameters (ParameterHandler &prm);

        /**
         * Read the parameters this class declares from the parameter file.
         */
        virtual
        void
        parse_parameters (ParameterHandler &prm);

    private:
      double compressibility;
      double melt_compressibility;
      double melt_bulk_modulus_derivative;
      bool use_bulk_density;
    };

  }
}

namespace aspect
{
  namespace MaterialModel
  {

    template <int dim>
    void
    DensityGradientApproximation<dim>::
    evaluate(const MaterialModel::MaterialModelInputs<dim> &in,
             MaterialModel::MaterialModelOutputs<dim> &out) const
    {
      MeltSimple<dim>::evaluate(in, out);

      // fill melt outputs if they exist
      MeltOutputs<dim> *melt_out = out.template get_additional_output<MeltOutputs<dim> >();

      if (melt_out != NULL)
        {
          for (unsigned int i=0; i < in.position.size(); ++i)
            {
              // the fluid compressibility includes two parts, a constant compressibility, and a pressure-dependent one
              // this is a simplified formulation, experimental data are often fit to the Birch-Murnaghan equation of state
              const double fluid_compressibility = melt_compressibility / (1.0 + in.pressure[i] * melt_bulk_modulus_derivative * melt_compressibility);
              double density, bulk_compressibility;

              if(use_bulk_density) // use the average of melt and solid density
                {
                  AssertThrow(this->introspection().compositional_name_exists("porosity"),
                              ExcMessage("Material model Melt simple with melt transport only "
                                         "works if there is a compositional field called porosity."));
                  const double porosity = in.composition[i][this->introspection().compositional_index_for_name("porosity")];

                  density = out.densities[i] * (1.0 - porosity) + melt_out->fluid_densities[i] * porosity;
                  bulk_compressibility = compressibility * (1.0 - porosity) + fluid_compressibility * porosity;
                }
              else // only use the solid density
                {
                  density = out.densities[i];
                  bulk_compressibility = compressibility;
                }

              melt_out->fluid_density_gradients[i] = density * melt_out->fluid_densities[i]
                                                     * bulk_compressibility
                                                     * this->get_gravity_model().gravity_vector(in.position[i]);
            }
        }
    }

    template <int dim>
    void
    DensityGradientApproximation<dim>::declare_parameters (ParameterHandler &prm)
    {
      MeltSimple<dim>::declare_parameters (prm);

      prm.enter_subsection("Material model");
        {
          prm.enter_subsection("Melt simple");
            {
              prm.declare_entry ("Solid compressibility", "0.0",
                                 Patterns::Double (0),
                                 "The value of the compressibility of the solid matrix. "
                                 "Units: $1/Pa$.");
              prm.declare_entry ("Melt compressibility", "0.0",
                                 Patterns::Double (0),
                                 "The value of the compressibility of the melt. "
                                 "Units: $1/Pa$.");
              prm.declare_entry ("Melt bulk modulus derivative", "0.0",
                                 Patterns::Double (0),
                                 "The value of the pressure derivative of the melt bulk"
                                 "modulus. "
                                 "Units: None.");
            }
          prm.leave_subsection();
          prm.enter_subsection("Density gradient approximation");
            {
              prm.declare_entry ("Use bulk density", "false",
                                 Patterns::Bool (),
                                 "If the bulk density should be used for compuing the fluid pressure"
                                 "gradient (if true), or only the solid density (if false). "
                                 "This controls the volume change of material with pressure.");
            }
          prm.leave_subsection();
        }
      prm.leave_subsection();
    }



    template <int dim>
    void
    DensityGradientApproximation<dim>::parse_parameters (ParameterHandler &prm)
    {
      MeltSimple<dim>::parse_parameters (prm);

      prm.enter_subsection("Material model");
        {
          prm.enter_subsection("Melt simple");
            {
              compressibility              = prm.get_double ("Solid compressibility");
              melt_compressibility         = prm.get_double ("Melt compressibility");
              melt_bulk_modulus_derivative = prm.get_double ("Melt bulk modulus derivative");
            }
          prm.leave_subsection();
          prm.enter_subsection("Density gradient approximation");
            {
              use_bulk_density             = prm.get_bool ("Use bulk density");
            }
          prm.leave_subsection();
        }
      prm.leave_subsection();
    }
  }
}

// explicit instantiations
namespace aspect
{
  namespace MaterialModel
  {
    ASPECT_REGISTER_MATERIAL_MODEL(DensityGradientApproximation,
                                   "density gradient approximation",
                                   "A material model that is like the "
                                   "'Melt imple' model, but implement different approximations "
                                   "for the gradient of the fluid density.")
  }
}

