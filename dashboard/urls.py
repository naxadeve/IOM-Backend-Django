from django.contrib import admin
from django.urls import path, include
from dashboard import views

urlpatterns = [
    path('home/', views.HomePage.as_view(), name='home'),
    path('create-user/', views.CreateUser, name='create-user'),
    path('reply-report/', views.report_reply, name='reply-report'),
    path('user-list/', views.UserList.as_view(), name='user-list'),
    path('activate/<int:id>', views.activate_user, name='activate'),
    path('delete/<str:model>/<int:id>/<str:url>', views.deleteData, name='delete'),
    path('delete_front/<str:model>/<int:id>/<str:url>', views.deleteDataFront, name='delete'),
    path('delete_dashboard/<str:model>/<int:id>/<str:url>', views.deleteDataDashboard, name='delete_dashboard'),

    path('upload-shapefile/', views.importShapefile, name='upload-shapefile'),
    path('openspace-list/<str:hlcit_code>', views.OpenSpaceList.as_view(), name='openspace-list'),
    path('community-space-list/<str:hlcit_code>', views.CommunitySpaceList.as_view(), name='community_space_list'),
    path('add-community-space-options/<str:hlcit_code>', views.AddCommunitySpaceOptions.as_view(),
         name='add_community_space_options'),
    path('openspace-add/<str:hlcit_code>', views.OpenSpaceCreate.as_view(), name='openspace-add'),
    path('openspace-edit/<int:pk>', views.OpenSpaceUpdate.as_view(), name='openspace-edit'),
    path('community-space-add/<str:hlcit_code>', views.CommunitySpaceCreate.as_view(), name='community_space_add'),
    path('community-space-edit/<int:pk>', views.CommunitySpaceUpdate.as_view(), name='community_space_update'),

    path('available-list/', views.AvailableFacilityList.as_view(), name='available-list'),
    path('available-add/', views.AvailableFacilityCreate.as_view(), name='available-add'),

    path('report-list/', views.ReportList.as_view(), name='report-list'),

    path('gallery-list/<int:id>', views.GalleryLists.as_view(), name='gallery-list'),
    path('gallery-add/<int:id>', views.GalleryCreate.as_view(), name='gallery-add'),
    path('gallery-edit/<int:pk>/<int:id>', views.GalleryUpdate.as_view(), name='gallery-edit'),

    path('question-list/', views.QuestionsList.as_view(), name='question-list'),
    path('question-add/', views.QuestionCreate.as_view(), name='question-add'),
    path('question-edit/<int:pk>', views.QuestionUpdate.as_view(), name='question-edit'),

    path('questiondata-list/<int:id>', views.QuestionData.as_view(), name='questiondata-list'),
    path('questiondata-add/<int:id>', views.QuestionDataCreate.as_view(), name='questiondata-add'),
    path('questiondata-edit/<int:pk>/<int:id>', views.QuestionDataUpdate.as_view(), name='questiondata-edit'),

    path('suggest-list/', views.SuggestedUseLists.as_view(), name='suggest-list'),
    path('suggest-add/', views.SuggestedCreate.as_view(), name='suggest-add'),
    path('suggest-edit/<int:pk>', views.SuggestedUpdate.as_view(), name='suggest-edit'),

    path('suggestdata-list/<int:id>', views.SuggestedUseDataList.as_view(), name='suggestdata-list'),
    path('suggestdata-add/<int:id>', views.SuggestedDataCreate.as_view(), name='suggestdata-add'),
    path('suggestdata-edit/<int:pk>/<int:id>', views.SuggestedDataUpdate.as_view(), name='suggestdata-edit'),

    path('service-list/', views.ServiceLists.as_view(), name='service-list'),
    path('service-add/', views.ServiceCreate.as_view(), name='service-add'),
    path('service-edit/<int:pk>', views.ServiceUpdate.as_view(), name='service-edit'),

    path('servicedata-list/<int:id>', views.ServiceDataList.as_view(), name='servicedata-list'),
    path('servicedata-add/<int:id>', views.ServiceDataCreate.as_view(), name='servicedata-add'),
    path('servicedata-edit/<int:pk>/<int:id>', views.ServiceDataUpdate.as_view(), name='servicedata-edit'),

    path('resource-list/', views.ResourceList.as_view(), name='resource-list'),
    path('resource-add/', views.ResourceCreate.as_view(), name='resource-add'),
    path('resource-edit/<int:pk>', views.ResourceUpdate.as_view(), name='resource-edit'),

    path('resource-category-list/', views.ResourceCategoryList.as_view(), name='resource-category-list'),
    path('resource-category-add/', views.ResourceCategoryCreate.as_view(), name='resource-category-add'),
    path('resource-category-edit/<int:pk>', views.ResourceCategoryUpdate.as_view(), name='resource-category-edit'),

    path('resource-document-list/', views.ResourceDocumentList.as_view(), name='resource-document-list'),
    path('resource-document-add/', views.ResourceDocumentTypeCreate.as_view(), name='resource-document-add'),
    path('resource-document-edit/<int:pk>', views.ResourceDocumentTypeUpdate.as_view(), name='resource-document-edit'),

    path('header-list/', views.HeaderList.as_view(), name='header-list'),
    path('header-update/<int:pk>', views.HeaderUpdate.as_view(), name='header-update'),
    path('slider-list/', views.SliderList.as_view(), name='slider-list'),
    path('slider-update/<int:pk>', views.SliderUpdate.as_view(), name='slider-update'),
    path('slider-add/', views.SliderCreate.as_view(), name='slider-create'),

    path('openspace-definition-list/', views.OpenSpaceDefinitionList.as_view(), name='openspace-definition-list'),
    path('openspace-definition-update/<int:pk>', views.OpenSpaceDefinitionUpdate.as_view(),
         name='openspace-definition-update'),

    path('openspace-identification-list/', views.OpenSpaceIdentificationList.as_view(),
         name='openspace-identification-list'),
    path('openspace-identification-update/<int:pk>', views.OpenSpaceIdentificationUpdate.as_view(),
         name='openspace-identification-update'),

    path('openspace-identification-process-list/', views.OpenSpaceIdentificationProcessList.as_view(),
         name='openspace-identification-process-list'),
    path('openspace-identification-process-update/<int:pk>', views.OpenSpaceIdentificationProcessUpdate.as_view(),
         name='openspace-identification-process-update'),
    path('openspace-identification-process-create/', views.OpenSpaceIdentificationProcessCreate.as_view(),
         name='openspace-identification-process-create'),

    path('footer-list/', views.FooterList.as_view(), name='footer-list'),
    path('footer-update/<int:pk>', views.FooterUpdate.as_view(), name='footer-update'),

    path('app-list/', views.AppList.as_view(), name='app-list'),
    path('app-add/', views.AppCreate.as_view(), name='app-add'),
    path('app-update/<int:pk>', views.AppUpdate.as_view(), name='app-update'),

    #home page list view
    path('home_page_list/', views.homePageListView, name='app-update'),

    path('open_new_list/', views.OpenSpaceMuniList.as_view(), name='open_muni'),

    path('amenity-type/<str:hlcit_code>', views.MunicipalityAmenityTypeList.as_view(),
         name='municipality_amenity_type'),
    path('amenity_type/', views.AmenityTypeList.as_view(),
         name='amenity_type'),

    path('municipality-available-amenities-list/<str:title>/<str:hlcit_code>',
         views.MunicipalityAvailableAmenityFacilityList.as_view(), name='municipality_available_ameni_list'),
    path('available_ameni_list/<str:title>/', views.AvailableAmenityFacilityList.as_view(),
         name='available_ameni_list'),
    path('amenity_type_add/', views.AvailableAmenityCreate.as_view(), name='amenity_type_add'),
    path('amenity_type_update/<int:pk>', views.AvailableAmenityUpdate.as_view(), name='amenity_type_update'),
    path('add-municipality-available-amenities/<str:hlcit_code>', views.AddBulkMunicipalityAvailableAmenities.as_view(),
         name='add_municipality_amenities'),

    path('create_agency/', views.create_agency, name='create_agency'),
    path('activate_agency/<int:id>/', views.activate_agency, name='activate_agency'),
    path('agency_list/', views.AgencyList.as_view(), name='agency_list'),

    path('agency_message/', views.AgencyMessageList.as_view(), name='agency_message'),
    path('agency_message_add/', views.AgencyMessageCreate.as_view(), name='agency_message_add'),
    path('agency_message_update/<int:pk>', views.AgencyMessageUpdate.as_view(), name='agency_message_update'),
    path('publish_report/<int:pk>', views.publish_report, name='publish_report'),

    path('about_page', views.aboutPageListView, name='about_page'),
    path('why_map_open_space_list', views.WhyMapOpenSpaceList.as_view(), name='why-openspace-list'),
    path('why_map_open_space_update/<int:pk>', views.WhyMapOpenSpaceUpdate.as_view(), name='why-openspace-list'),

    path('why_map_open_icon_list', views.WhyMapOpenSpaceIconList.as_view(), name='why-openicon-list'),
    path('why_map_open_icon_update/<int:pk>', views.WhyMapOpenSpaceIconUpdate.as_view(), name='why-openspace-update'),
    path('why_map_open_icon_add/', views.WhyMapOpenSpaceIconCreate.as_view(), name='why-openspace-add'),


    path('about_header_list/', views.AboutHeaderList.as_view(), name='about-header-list'),
    path('about_header_update/<int:pk>', views.AboutHeaderUpdate.as_view(), name='about-header-update'),

    path('open_criteria_list/', views.OpenSpaceCriteriaList.as_view(), name='openspace-criteria-list'),
    path('open_criteria_update/<int:pk>', views.OpenSpaceCriteriaUpdate.as_view(), name='openspace-criteria-update'),


    path('about_criteria_type_list/', views.AboutCriteriaTypeList.as_view(), name='about-criteria-type-list'),
    path('about_criteria_type_add/', views.AboutCriteriaTypeCreate.as_view(), name='about-criteria-type-add'),
    path('about_criteria_type_update/<int:pk>', views.AboutCriteriaTypeUpdate.as_view(), name='about-criteria-type-update'),


    path('about_criteria_type_description_list/<str:criteria_type>', views.AboutCriteriaTypeDescriptionList.as_view(), name='about-criteria-type-des-list'),
    path('about_criteria_type_description_add/<str:criteria_type>', views.AboutCriteriaTypeDescriptionCreate.as_view(), name='about-criteria-type-description-add'),
    path('about_criteria_type_description_update/<int:pk>/<str:criteria_type>', views.AboutCriteriaTypeDescriptionUpdate.as_view(), name='about-criteria-type-description-update'),


    path('open_space_identification_points_list/<str:title>', views.OpenSpaceIdentificationPointList.as_view(), name='open-space-identification-point-list'),
    path('open_space_identification_points_add/<str:title>', views.OpenSpaceIdentificationPointsCreate.as_view(), name='open-space-identification-point-add'),
    path('open_space_identification_points_update/<int:pk>/<str:title>', views.OpenSpaceIdentificationPointsUpdate.as_view(), name='open-space-identification-point-update'),



    path('bulk_open_space_upload', views.uploadOpenSpaceFile, name='about_page'),
    path('add-new-location', views.MainOpenSpaceView.as_view(), name='add_new_location'),
    path('bulk-upload-community-space/<str:hlcit_code>', views.BulkUploadCommunitySpaceView.as_view(),
         name='bulk_upload_community_space'),

    path('add-available-facility/<str:available_type>/<str:hlcit_code>', views.AddMunicipalityAvailableAmenity.as_view(),
         name='add_available_facility'),
    path('update-available-facility/<int:pk>', views.UpdateMunicipalityAvailableAmenity.as_view(),
         name='update_available_facility'),

    path('eia/<str:hlcit_code>', views.EiaFromMunicipalityListView.as_view(),
         name='list_eia_from_municipality'),

    path('add-eia/<str:hlcit_code>', views.BulkAddEiaFromMunicipalityView.as_view(),
         name='add_eia_from_municipality'),

    path('update-eia/<int:pk>', views.BulkUpdateEiaFromMunicipalityView.as_view(),
         name='update_eia_from_municipality'),

    path('delete-municipality-available-type/<int:id>', views.delete_municipality_available_type,
         name='delete_municipality_available_type'),

    path('edit-available-type/<int:id>', views.edit_municipality_available_type,
         name='edit_municipality_available_type'),

    path('delete-municipality-eia/<int:id>', views.delete_municipality_eia, name='delete_municipality_eia'),

]
