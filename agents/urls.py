from django.urls import path
from agents.views import Agents

urlpatterns = [
    path('start_workflow/', Agents.as_view({"post": "fitness"}), name='fitness_agent'),
]


# urlpatterns = [
#     path("price_range", Vaults.as_view({"get": "price_range"})),
#     path("expiration", Vaults.as_view({"get": "expiration"})),
#     path("asset_tvl", Vaults.as_view({"get": "asset_tvl"})),
#     path("total_tvl", Vaults.as_view({"get": "total_tvl"})),
#     path("strategy_plot_data", Vaults.as_view({"get": "strategy_plot_data"})),
#     path("asset_apy", Vaults.as_view({"get": "asset_apy"})),
# ]
