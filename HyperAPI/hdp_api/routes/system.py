from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class System(Resource):
    name = "System"
    available_since = "1.0"
    removed_since = None

    class _features(Route):
        name = "features"
        httpMethod = Route.GET
        path = "/system/features"

    class _products(Route):
        name = "products"
        httpMethod = Route.GET
        path = "/system/products"

    class _About(Route):
        name = "About"
        httpMethod = Route.GET
        path = "/system/about"

    class _Menu(Route):
        name = "Menu"
        httpMethod = Route.GET
        path = "/system/menu"

    class _userAllowedResource(Route):
        name = "userAllowedResource"
        httpMethod = Route.GET
        path = "/system/userAllowedResource"

    class _personalApps(Route):
        name = "personalApps"
        httpMethod = Route.GET
        path = "/system/personalApps"
