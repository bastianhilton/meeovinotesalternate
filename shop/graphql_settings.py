from .settings import *

GRAPHENE_GENERATOR_MODELS = [
    { 'name': 'AddressCountry', 'path': 'shop.models.AddressCountry', 'path': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AddressUseraddress', 'path': 'shop.models.AddressUseraddress', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AdvancedFiltersAdvancedfilter', 'path': 'shop.models.AdvancedFiltersAdvancedfilter', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AdvancedFiltersAdvancedfilterGroups', 'path': 'shop.models.AdvancedFiltersAdvancedfilterGroups', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AdvancedFiltersAdvancedfilterUsers', 'path': 'shop.models.AdvancedFiltersAdvancedfilterUsers', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AldrynFormsEmailfieldplugin', 'path': 'shop.models.AldrynFormsEmailfieldplugin', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AldrynFormsEmailfieldplugin', 'path': 'shop.models.AldrynFormsEmailfieldplugin', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AldrynFormsFieldplugin', 'path': 'shop.models.AldrynFormsFieldplugin', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AldrynFormsFieldsetplugin', 'path': 'shop.models.AldrynFormsFieldsetplugin', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AldrynFormsFileuploadfieldplugin', 'path': 'shop.models.AldrynFormsFileuploadfieldplugin', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AldrynFormsFormbuttonplugin', 'path': 'shop.models.AldrynFormsFormbuttonplugin', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AldrynFormsFormplugin', 'path': 'shop.models.AldrynFormsFormplugin', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AldrynFormsFormpluginRecipients', 'path': 'shop.models.AldrynFormsFormpluginRecipients', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AldrynFormsFormsubmission', 'path': 'shop.models.AldrynFormsFormsubmission', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AldrynFormsImageuploadfieldplugin', 'path': 'shop.models.AldrynFormsImageuploadfieldplugin', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AldrynFormsOption', 'path': 'shop.models.AldrynFormsOption', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AldrynFormsTextareafieldplugin', 'path': 'shop.models.AldrynFormsTextareafieldplugin', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AnalyticsProductrecord', 'path': 'shop.models.AnalyticsProductrecord', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AnalyticsUserproductview', 'path': 'shop.models.AnalyticsUserproductview', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AnalyticsUserrecord', 'path': 'shop.models.AnalyticsUserrecord', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AnalyticsUsersearch', 'path': 'shop.models.AnalyticsUsersearch', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AnnouncementsAnnouncement', 'path': 'shop.models.AnnouncementsAnnouncement', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AnnouncementsDismissal', 'path': 'shop.models.AnnouncementsDismissal', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AuthGroup', 'path': 'shop.models.AuthGroup', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AuthGroupPermissions', 'path': 'shop.models.AuthGroupPermissions', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AuthPermission', 'path': 'shop.models.AuthPermission', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AuthUser', 'path': 'shop.models.AuthUser', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AuthUserGroups', 'path': 'shop.models.AuthUserGroups', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'AuthUserUserPermissions', 'path': 'shop.models.AuthUserUserPermissions', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'BasketBasket', 'path': 'shop.models.BasketBasket', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'BasketBasketVouchers', 'path': 'shop.models.BasketBasketVouchers', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'BasketLine', 'path': 'shop.models.BasketLine', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'BasketLineattribute', 'path': 'shop.models.BasketLineattribute', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4AlertsBootstrap4Alerts', 'path': 'shop.models.Bootstrap4AlertsBootstrap4Alerts', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4BadgeBootstrap4Badge', 'path': 'shop.models.Bootstrap4BadgeBootstrap4Badge', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4CardBootstrap4Card', 'path': 'shop.models.Bootstrap4CardBootstrap4Card', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4CardBootstrap4Cardinner', 'path': 'shop.models.Bootstrap4CardBootstrap4Cardinner', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4CarouselBootstrap4Carousel', 'path': 'shop.models.Bootstrap4CarouselBootstrap4Carousel', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4CarouselBootstrap4Carouselslide', 'path': 'shop.models.Bootstrap4CarouselBootstrap4Carouselslide', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4CollapseBootstrap4Collapse', 'path': 'shop.models.Bootstrap4CollapseBootstrap4Collapse', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4CollapseBootstrap4Collapsecontainer', 'path': 'shop.models.Bootstrap4CollapseBootstrap4Collapsecontainer', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4CollapseBootstrap4Collapsetrigger', 'path': 'shop.models.Bootstrap4CollapseBootstrap4Collapsetrigger', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4ContentBootstrap4Blockquote', 'path': 'shop.models.Bootstrap4ContentBootstrap4Blockquote', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4ContentBootstrap4Code', 'path': 'shop.models.Bootstrap4ContentBootstrap4Code', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4ContentBootstrap4Figure', 'path': 'shop.models.Bootstrap4ContentBootstrap4Figure', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4GridBootstrap4Gridcolumn', 'path': 'shop.models.Bootstrap4GridBootstrap4Gridcolumn', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4GridBootstrap4Gridcontainer', 'path': 'shop.models.Bootstrap4GridBootstrap4Gridcontainer', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4GridBootstrap4Gridrow', 'path': 'shop.models.Bootstrap4GridBootstrap4Gridrow', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4JumbotronBootstrap4Jumbotron', 'path': 'shop.models.Bootstrap4JumbotronBootstrap4Jumbotron', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4LinkBootstrap4Link', 'path': 'shop.models.Bootstrap4LinkBootstrap4Link', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4ListgroupBootstrap4Listgroup', 'path': 'shop.models.Bootstrap4ListgroupBootstrap4Listgroup', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4ListgroupBootstrap4Listgroupitem', 'path': 'shop.models.Bootstrap4ListgroupBootstrap4Listgroupitem', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4MediaBootstrap4Media', 'path': 'shop.models.Bootstrap4MediaBootstrap4Media', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4MediaBootstrap4Mediabody', 'path': 'shop.models.Bootstrap4MediaBootstrap4Mediabody', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4PictureBootstrap4Picture', 'path': 'shop.models.Bootstrap4PictureBootstrap4Picture', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4TabsBootstrap4Tab', 'path': 'shop.models.Bootstrap4TabsBootstrap4Tab', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4TabsBootstrap4Tabitem', 'path': 'shop.models.Bootstrap4TabsBootstrap4Tabitem', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Bootstrap4UtilitiesBootstrap4Spacing', 'path': 'shop.models.Bootstrap4UtilitiesBootstrap4Spacing', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CatalogueAttributeoption', 'path': 'shop.models.CatalogueAttributeoption', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CatalogueAttributeoptiongroup', 'path': 'shop.models.CatalogueAttributeoptiongroup', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CatalogueCategory', 'path': 'shop.models.CatalogueCategory', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CatalogueOption', 'path': 'shop.models.CatalogueOption', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CatalogueProduct', 'path': 'shop.models.CatalogueProduct', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CatalogueProductattribute', 'path': 'shop.models.CatalogueProductattribute', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CatalogueProductattributevalue', 'path': 'shop.models.CatalogueProductattributevalue', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CatalogueProductattributevalueValueMultiOption', 'path': 'shop.models.CatalogueProductattributevalueValueMultiOption', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CatalogueProductcategory', 'path': 'shop.models.CatalogueProductcategory', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CatalogueProductclass', 'path': 'shop.models.CatalogueProductclass', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CatalogueProductclassOptions', 'path': 'shop.models.CatalogueProductclassOptions', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CatalogueProductimage', 'path': 'shop.models.CatalogueProductimage', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CatalogueProductProductOptions', 'path': 'shop.models.CatalogueProductProductOptions', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CatalogueProductrecommendation', 'path': 'shop.models.CatalogueProductrecommendation', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Client', 'path': 'shop.models.Client', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CmsAliaspluginmodel', 'path': 'shop.models.CmsAliaspluginmodel', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CmsCmsplugin', 'path': 'shop.models.CmsCmsplugin', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CmsGlobalpagepermission', 'path': 'shop.models.CmsGlobalpagepermission', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CmsGlobalpagepermissionSites', 'path': 'shop.models.CmsGlobalpagepermissionSites', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CmsPage', 'path': 'shop.models.CmsPage', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CmsPagepermission', 'path': 'shop.models.CmsPagepermission', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CmsPagePlaceholders', 'path': 'shop.models.CmsPagePlaceholders', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CmsPageuser', 'path': 'shop.models.CmsPageuser', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CmsPageusergroup', 'path': 'shop.models.CmsPageusergroup', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CmsPlaceholder', 'path': 'shop.models.CmsPlaceholder', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CmsPlaceholderreference', 'path': 'shop.models.CmsPlaceholderreference', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CmsStaticplaceholder', 'path': 'shop.models.CmsStaticplaceholder', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CmsTitle', 'path': 'shop.models.CmsTitle', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CmsTreenode', 'path': 'shop.models.CmsTreenode', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CmsUrlconfrevision', 'path': 'shop.models.CmsUrlconfrevision', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CmsUsersettings', 'path': 'shop.models.CmsUsersettings', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CommunicationCommunicationeventtype', 'path': 'shop.models.CommunicationCommunicationeventtype', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CommunicationEmail', 'path': 'shop.models.CommunicationEmail', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CommunicationNotification', 'path': 'shop.models.CommunicationNotification', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'CustomerProductalert', 'path': 'shop.models.CustomerProductalert', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangoAdminLog', 'path': 'shop.models.DjangoAdminLog', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsBlogAuthorentriesplugin', 'path': 'shop.models.DjangocmsBlogAuthorentriesplugin', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsBlogAuthorentriespluginAuthors', 'path': 'shop.models.DjangocmsBlogAuthorentriespluginAuthors', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsBlogBlogcategory', 'path': 'shop.models.DjangocmsBlogBlogcategory', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsBlogBlogcategoryTranslation', 'path': 'shop.models.DjangocmsBlogBlogcategoryTranslation', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsBlogBlogconfig', 'path': 'shop.models.DjangocmsBlogBlogconfig', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsBlogBlogconfigTranslation', 'path': 'shop.models.DjangocmsBlogBlogconfigTranslation', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsBlogGenericblogplugin', 'path': 'shop.models.DjangocmsBlogGenericblogplugin', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsBlogLatestpostsplugin', 'path': 'shop.models.DjangocmsBlogLatestpostsplugin', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsBlogLatestpostspluginCategories', 'path': 'shop.models.DjangocmsBlogLatestpostspluginCategories', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsBlogPost', 'path': 'shop.models.DjangocmsBlogPost', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsBlogPostCategories', 'path': 'shop.models.DjangocmsBlogPostCategories', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsBlogPostRelated', 'path': 'shop.models.DjangocmsBlogPostRelated', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsBlogPostSites', 'path': 'shop.models.DjangocmsBlogPostSites', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsBlogPostTranslation', 'path': 'shop.models.DjangocmsBlogPostTranslation', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsFileFile', 'path': 'shop.models.DjangocmsFileFile', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsFileFolder', 'path': 'shop.models.DjangocmsFileFolder', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsGooglemapGooglemap', 'path': 'shop.models.DjangocmsGooglemapGooglemap', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsGooglemapGooglemapmarker', 'path': 'shop.models.DjangocmsGooglemapGooglemapmarker', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsGooglemapGooglemaproute', 'path': 'shop.models.DjangocmsGooglemapGooglemaproute', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsHistoryPlaceholderaction', 'path': 'shop.models.DjangocmsHistoryPlaceholderaction', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsHistoryPlaceholderoperation', 'path': 'shop.models.DjangocmsHistoryPlaceholderoperation', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsIconIcon', 'path': 'shop.models.DjangocmsIconIcon', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsLinkLink', 'path': 'shop.models.DjangocmsLinkLink', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsMapsMaps', 'path': 'shop.models.DjangocmsMapsMaps', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsPicturePicture', 'path': 'shop.models.DjangocmsPicturePicture', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsStyleStyle', 'path': 'shop.models.DjangocmsStyleStyle', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsTextCkeditorText', 'path': 'shop.models.DjangocmsTextCkeditorText', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsVideoVideoplayer', 'path': 'shop.models.DjangocmsVideoVideoplayer', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsVideoVideosource', 'path': 'shop.models.DjangocmsVideoVideosource', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangocmsVideoVideotrack', 'path': 'shop.models.DjangocmsVideoVideotrack', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangoContent', 'path': 'shop.models.DjangoContent', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangoFlatpage', 'path': 'shop.models.DjangoFlatpage', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangoFlatpageSites', 'path': 'shop.models.DjangoFlatpageSites', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangoMigrations', 'path': 'shop.models.DjangoMigrations', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangoSession', 'path': 'shop.models.DjangoSession', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'DjangoSite', 'path': 'shop.models.DjangoSite', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'EasyThumbnailsSource', 'path': 'shop.models.EasyThumbnailsSource', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'EasyThumbnailsThumbnail', 'path': 'shop.models.EasyThumbnailsThumbnail', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'EasyThumbnailsThumbnaildimensions', 'path': 'shop.models.EasyThumbnailsThumbnaildimensions', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'FilerClipboard', 'path': 'shop.models.FilerClipboard', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'FilerClipboarditem', 'path': 'shop.models.FilerClipboarditem', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'FilerFile', 'path': 'shop.models.FilerFile', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'FilerFolder', 'path': 'shop.models.FilerFolder', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'FilerFolderpermission', 'path': 'shop.models.FilerFolderpermission', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'FilerImage', 'path': 'shop.models.FilerImage', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'FilerThumbnailoption', 'path': 'shop.models.FilerThumbnailoption', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'MenusCachekey', 'path': 'shop.models.MenusCachekey', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OfferBenefit', 'path': 'shop.models.OfferBenefit', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OfferCondition', 'path': 'shop.models.OfferCondition', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OfferConditionaloffer', 'path': 'shop.models.OfferConditionaloffer', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OfferConditionalofferCombinations', 'path': 'shop.models.OfferConditionalofferCombinations', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OfferRange', 'path': 'shop.models.OfferRange', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OfferRangeClasses', 'path': 'shop.models.OfferRangeClasses', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OfferRangeExcludedProducts', 'path': 'shop.models.OfferRangeExcludedProducts', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OfferRangeIncludedCategories', 'path': 'shop.models.OfferRangeIncludedCategories', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OfferRangeproduct', 'path': 'shop.models.OfferRangeproduct', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OfferRangeproductfileupload', 'path': 'shop.models.OfferRangeproductfileupload', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OrderBillingaddress', 'path': 'shop.models.OrderBillingaddress', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OrderCommunicationevent', 'path': 'shop.models.OrderCommunicationevent', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OrderLine', 'path': 'shop.models.OrderLine', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OrderLineattribute', 'path': 'shop.models.OrderLineattribute', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OrderLineprice', 'path': 'shop.models.OrderLineprice', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OrderOrder', 'path': 'shop.models.OrderOrder', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OrderOrderdiscount', 'path': 'shop.models.OrderOrderdiscount', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OrderOrdernote', 'path': 'shop.models.OrderOrdernote', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OrderOrderstatuschange', 'path': 'shop.models.OrderOrderstatuschange', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OrderPaymentevent', 'path': 'shop.models.OrderPaymentevent', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OrderPaymenteventquantity', 'path': 'shop.models.OrderPaymenteventquantity', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OrderPaymenteventtype', 'path': 'shop.models.OrderPaymenteventtype', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OrderShippingaddress', 'path': 'shop.models.OrderShippingaddress', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OrderShippingevent', 'path': 'shop.models.OrderShippingevent', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OrderShippingeventquantity', 'path': 'shop.models.OrderShippingeventquantity', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OrderShippingeventtype', 'path': 'shop.models.OrderShippingeventtype', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OrderSurcharge', 'path': 'shop.models.OrderSurcharge', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OscarapiApikey', 'path': 'shop.models.OscarapiApikey', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OscarInvoicesInvoice', 'path': 'shop.models.OscarInvoicesInvoice', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OscarInvoicesLegalentity', 'path': 'shop.models.OscarInvoicesLegalentity', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'OscarInvoicesLegalentityaddress', 'path': 'shop.models.OscarInvoicesLegalentityaddress', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PartnerPartner', 'path': 'shop.models.PartnerPartner', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PartnerPartneraddress', 'path': 'shop.models.PartnerPartneraddress', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PartnerPartnerUsers', 'path': 'shop.models.PartnerPartnerUsers', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PartnerStockalert', 'path': 'shop.models.PartnerStockalert', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PartnerStockrecord', 'path': 'shop.models.PartnerStockrecord', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Payment', 'path': 'shop.models.Payment', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PaymentBankcard', 'path': 'shop.models.PaymentBankcard', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PaymentSource', 'path': 'shop.models.PaymentSource', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PaymentSourcetype', 'path': 'shop.models.PaymentSourcetype', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PaymentTransaction', 'path': 'shop.models.PaymentTransaction', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PaypalExpresstransaction', 'path': 'shop.models.PaypalExpresstransaction', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PaypalPayflowtransaction', 'path': 'shop.models.PaypalPayflowtransaction', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PhotologueGallery', 'path': 'shop.models.PhotologueGallery', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PhotologueGalleryPhotos', 'path': 'shop.models.PhotologueGalleryPhotos', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PhotologueGallerySites', 'path': 'shop.models.PhotologueGallerySites', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PhotologuePhoto', 'path': 'shop.models.PhotologuePhoto', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PhotologuePhotoeffect', 'path': 'shop.models.PhotologuePhotoeffect', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PhotologuePhotoSites', 'path': 'shop.models.PhotologuePhotoSites', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PhotologuePhotosize', 'path': 'shop.models.PhotologuePhotosize', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PhotologueWatermark', 'path': 'shop.models.PhotologueWatermark', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PinaxBadgesBadgeaward', 'path': 'shop.models.PinaxBadgesBadgeaward', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PinaxEventsEvent', 'path': 'shop.models.PinaxEventsEvent', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PinaxMessagesMessage', 'path': 'shop.models.PinaxMessagesMessage', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PinaxMessagesThread', 'path': 'shop.models.PinaxMessagesThread', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'PinaxMessagesUserthread', 'path': 'shop.models.PinaxMessagesUserthread', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'Product', 'path': 'shop.models.Product', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'ReviewsProductreview', 'path': 'shop.models.ReviewsProductreview', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'ReviewsVote', 'path': 'shop.models.ReviewsVote', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'SalesLineTransaction', 'path': 'shop.models.SalesLineTransaction', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'ShippingOrderanditemcharges', 'path': 'shop.models.ShippingOrderanditemcharges', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'ShippingOrderanditemchargesCountries', 'path': 'shop.models.ShippingOrderanditemchargesCountries', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'ShippingWeightband', 'path': 'shop.models.ShippingWeightband', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'ShippingWeightbased', 'path': 'shop.models.ShippingWeightbased', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'ShippingWeightbasedCountries', 'path': 'shop.models.ShippingWeightbasedCountries', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'TaggitTag', 'path': 'shop.models.TaggitTag', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'TaggitTaggeditem', 'path': 'shop.models.TaggitTaggeditem', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'TestimonialsTestimonial', 'path': 'shop.models.TestimonialsTestimonial', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'ThumbnailKvstore', 'path': 'shop.models.ThumbnailKvstore', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'VoucherVoucher', 'path': 'shop.models.VoucherVoucher', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'VoucherVoucherapplication', 'path': 'shop.models.VoucherVoucherapplication', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'VoucherVoucherOffers', 'path': 'shop.models.VoucherVoucherOffers', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'VoucherVoucherset', 'path': 'shop.models.VoucherVoucherset', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'WishlistsLine', 'path': 'shop.models.WishlistsLine', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
    { 'name': 'WishlistsWishlist', 'path': 'shop.models.WishlistsWishlist', 'require_auth': { 'queries': ["all", "single"], 'mutations': ["create", 'update', 'delete'] } },
]