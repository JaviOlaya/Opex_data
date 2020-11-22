from django.contrib import admin
from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    
    path("lista_proyectos/", views.ListProyecto.as_view(), name="proyectos"),
    path("lista_personal/", views.ListPersonal.as_view(), name="Lpersonal"),
    path("lista_g_admin/", views.ListGastoAdministrativo.as_view(), name="gadmin"),
    path('list_electric_cost/',views.ListElectricCost.as_view(), name='listElectricCost'),
    path('list_gas_cost/',views.ListGasCost.as_view(), name='listGascost'),
    path('list_fertilizer_cost/',views.ListFertilizerCost.as_view(), name='listFertilizercost'),
    path('list_substrate_cost/',views.ListSubstrateCost.as_view(), name='listSubstratecost'),
    path('list_shipping_cost/',views.ListShippingCost.as_view(), name='listShippingCost'),
    path('list_seeds_cost/',views.ListSeedsCost.as_view(), name='listSeedsCost'),
    path('list_fuel_cost/',views.ListFuelCost.as_view(), name='listFuelCost'),
    path('list_cleaning_cost/',views.ListCleaningCost.as_view(), name='listCleaningCost'),
    path('list_various_cost/',views.ListVariousCost.as_view(), name='listVariousCost'),
    path('list_tax_rate/',views.ListTaxRate.as_view(), name='listTaxRate'),
    path('list_remedy/',views.ListRemedyCost.as_view(), name='listRemedy'),
    path('list_Macro_Ind/',views.ListMacroeconomicsIndicator.as_view(), name='listMacroind'),
    path('detail_project/<pk>',views.ProyectoDetailView.as_view(), name='project_detail'),
    path('detail_personal_cost/<pk>',views.PersonalDetailView.as_view(), name='staff_detail'),
    path('detail_admin_cost/<pk>',views.ListGastoAdministrativoDetailView.as_view(), name='admincost_detail'),
    path('detail_electric_cost/<pk>',views.ElectricCostDetailView.as_view(), name='electricCost_detail'),
    path('detail_gas_cost/<pk>',views.GasCostDetailView.as_view(), name='gasCost_detail'),
    path('detail_fertilizer_cost/<pk>',views.FertilizerCostDetailView.as_view(), name='fertilizerCost_detail'),
    path('detail_substrate_cost/<pk>',views.SubstrateCostDetailView.as_view(), name='substrateCost_detail'),
    path('detail_shipping_cost/<pk>',views.ShippingCostDetailView.as_view(), name='shippingCost_detail'),
    path('detail_seeds_cost/<pk>',views.SeedsCostDetailView.as_view(), name='seedsCost_detail'),
    path('detail_fuel_cost/<pk>',views.FuelCostDetailView.as_view(), name='fuelCost_detail'),
    path('detail_cleaning_cost/<pk>',views.CleaningCostDetailView.as_view(), name='cleaningCost_detail'),
    path('detail_various_cost/<pk>',views.VariousCostDetailView.as_view(), name='variousCost_detail'),
    path('detail_tax_rate/<pk>',views.TaxRateDetailView.as_view(), name='taxRate_detail'),
     path('detail_remedy/<pk>',views.RemedioDetailView.as_view(), name='remedy_detail'),
    path('detail_macEcInd/<pk>',views.MacroeconomicsIndicatorDetailView.as_view(), name='macEcInd_detail'),
    path("data_analysis/", views.DataAnalysisView.as_view(), name="analisis")
    # path("pagina/<str:slug>", views.page, name="page"),
]