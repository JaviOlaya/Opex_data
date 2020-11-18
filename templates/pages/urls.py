from django.contrib import admin
from django.urls import path
from . import views
app_name = "inputapp"

urlpatterns = [
 
    path('add_project/',views.ProyectosCreateView.as_view(), name='addProject'),
    path('update_project/<pk>/',views.ProyectosUpdateView.as_view(), name='updateProject'),
    path('delete_project/<pk>/',views.ProyectosDeleteView.as_view(), name='deleteProject'),
    
    path('add_staff/',views.PersonalCreateView.as_view(), name='addStaff'),
    path('update_staff/<pk>/',views.PersonalUpdateView.as_view(), name='updateStaff'),
    path('delete_staff/<pk>/',views.PersonalDeleteView.as_view(), name='deleteStaff'),
    
    path('add_admin_cost/',views.AdminCostCreateView.as_view(), name='addadmin_cost'),
    path('update_admin_cost/<pk>/',views.AdminCostUpdateView.as_view(), name='updateadmin_cost'),
    path('delete_admin_cost/<pk>/',views.AdminCostDeleteView.as_view(), name='deleteadmin_cost'),
    
    path('add_electric_cost/',views.ElectricCostCreateView.as_view(), name='addElectricCost'),
    path('update_electric_cost/<pk>/',views.ElectricCostUpdateView.as_view(), name='updateElectricCost'),
    path('delete_electric_cost/<pk>/',views.ElectricCostDeleteView.as_view(), name='deleteElectricCost'),
   
    path('add_gas_cost/',views.GasCostCreateView.as_view(), name='addGascost'),
    path('update_gas_cost/<pk>/',views.GasCostUpdateView.as_view(), name='updateGascost'),
    path('delete_gas_cost/<pk>/',views.GasCostDeleteView.as_view(), name='deleteGascost'),
    
    path('add_fertilizer_cost/',views.FertilizerCostCreateView.as_view(), name='addFertilizercost'),
    path('update_fertilizer_cost/<pk>/',views.FertilizerCostUpdateView.as_view(), name='updateFertilizercost'),
    path('delete_fertilizer_cost/<pk>/',views.FertilizerCostDeleteView.as_view(), name='deleteFertilizercost'),
    
    path('add_substrate_cost/',views.SubstrateCostCreateView.as_view(), name='addSubstratecost'),
    path('update_substrate_cost/<pk>/',views.SubstrateCostUpdateView.as_view(), name='updateSubstratecost'),
    path('delete_substrate_cost/<pk>/',views.SubstrateCostDeleteView.as_view(), name='deleteSubstratecost'),
  
    path('add_shipping_cost/',views.ShippingCostCreateView.as_view(), name='addShippingCost'),
    path('update_shipping_cost/<pk>/',views.ShippingCostUpdateView.as_view(), name='updateShippingCost'),
    path('delete_shipping_cost/<pk>/',views.ShippingCostDeleteView.as_view(), name='deleteShippingCost'),
    
    path('add_seeds_cost/',views.SeedsCostCreateView.as_view(), name='addSeedsCost'),
    path('update_seeds_cost/<pk>/',views.SeedsCostUpdateView.as_view(), name='updateSeedsCost'),
    path('delete_seeds_cost/<pk>/',views.SeedsCostDeleteView.as_view(), name='deleteSeedsCost'),
   
    path('add_fuel_cost/',views.FuelCostCreateView.as_view(), name='addFuelCost'),
    path('update_fuel_cost/<pk>/',views.FuelCostUpdateView.as_view(), name='updateFuelCost'),
    path('delete_fuel_cost/<pk>/',views.FuelCostDeleteView, name='deleteFuelCost'),
    
    path('add_cleaning_cost/',views.FuelCostCreateView.as_view(), name='addCleaningCost'),
    path('update_cleaning_cost/<pk>/',views.FuelCostUpdateView.as_view(), name='updateCleaningCost'),
    path('delete_cleaning_cost/<pk>/',views.FuelCostDeleteView.as_view(), name='deleteCleaningCost'),
   
    path('add_remedies_cost/',views.RemediesCostCreateView.as_view(), name='addRemediesCost'),
    path('update_remedies_cost/<pk>/',views.RemediesCostUpdateView.as_view(), name='updateRemediesCost'),
    path('delete_remedies_cost/<pk>/',views.RemediesCostDeleteView.as_view(), name='deleteRemediesCost'),
   
    path('add_various_cost/',views.VariousCostCreateView.as_view(), name='addVariousCost'),
    path('update_various_cost/<pk>/',views.VariousCostUpdateView.as_view(), name='updateVariousCost'),
    path('delete_various_cost/<pk>/',views.VariousCostDeleteView.as_view(), name='deleteVariousCost'),
    
    path('add_Macro_Ind/',views.MacroeconomicsIndicatorsCreateView.as_view(), name='macroIndi'),
    path('update_various_cost/<pk>/',views.MacroeconomicsIndicatorsUpdateView.as_view(), name='updateMacroIndi'),
    path('delete_various_cost/<pk>/',views.MacroeconomicsIndicatorsDeleteView.as_view(), name='deleteMacroIndi'),
    
    path('add_tax_rate/',views.taxRateCreateView.as_view(), name='addTaxRate'),
    path('update_tax_rate/<pk>/',views.taxRateUpdateView.as_view(), name='updateTaxRate'),
    path('delete_tax_rate/<pk>/',views.taxRateDeleteView.as_view(), name='deleteTaxRate'),
    
    # path('success/', views.SuccesView.as_view(),name="correcto"),
    path('success/', views.SuccesView.as_view(),name="correcto")

]