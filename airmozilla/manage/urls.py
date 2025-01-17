from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^/?$', views.dashboard, name='home'),
    url(r'^users/(?P<id>\d+)/$', views.user_edit, name='user_edit'),
    url(r'^users/$', views.users, name='users'),
    url(r'^users/data/$', views.users_data, name='users_data'),
    url(r'^groups/(?P<id>\d+)/$', views.group_edit, name='group_edit'),
    url(r'^groups/remove/(?P<id>\d+)/$', views.group_remove,
        name='group_remove'),
    url(r'^groups/new/$', views.group_new, name='group_new'),
    url(r'^groups/$', views.groups, name='groups'),
    url(r'^events/request/$', views.event_request, name='event_request'),
    url(r'^events/(?P<id>\d+)/$', views.event_edit, name='event_edit'),
    url(r'^events/(?P<id>\d+)/assignment/$',
        views.event_assignment,
        name='event_assignment'),
    url(r'^events/(?P<id>\d+)/transcript/$',
        views.event_transcript,
        name='event_transcript'),
    url(r'^events/(?P<id>\d+)/upload/$',
        views.event_upload,
        name='event_upload'),
    url(r'^events/(?P<id>\d+)/vidly-submissions/$',
        views.event_vidly_submissions,
        name='event_vidly_submissions'),
    url(r'^events/(?P<id>\d+)/vidly-submissions/submission'
        r'/(?P<submission_id>\d+)/$',
        views.event_vidly_submission,
        name='event_vidly_submission'),
    url(r'^events/(?P<id>\d+)/comments/$',
        views.event_comments,
        name='event_comments'),
    url(r'^events/(?P<id>\d+)/comments/configuration/$',
        views.event_discussion,
        name='event_discussion'),
    url(r'^events/(?P<id>\d+)/stop-live/$', views.event_stop_live,
        name='stop_live_event'),
    url(r'^events/(?P<id>\d+)/survey/$', views.event_survey,
        name='event_survey'),
    url(r'^events/(?P<id>\d+)/tweets/$', views.event_tweets,
        name='event_tweets'),
    url(r'^events/(?P<id>\d+)/tweets/new/$', views.new_event_tweet,
        name='new_event_tweet'),
    url(r'^events/all/tweets/$', views.all_event_tweets,
        name='all_event_tweets'),
    url(r'^events/archive/(?P<id>\d+)/$', views.event_archive,
        name='event_archive'),
    url(r'^events/archive/(?P<id>\d+)/auto/$',
        views.event_archive_auto,
        name='event_archive_auto'),
    url(r'^events/duplicate/(?P<duplicate_id>\d+)/$', views.event_request,
        name='event_duplicate'),
    url(r'^events/vidlyurltoshortcode/(?P<id>\d+)/',
        views.vidly_url_to_shortcode,
        name='vidly_url_to_shortcode'),
    url(r'^events/hits/$', views.event_hit_stats, name='event_hit_stats'),
    url(r'^events/assignments/$',
        views.event_assignments,
        name='event_assignments'),
    url(r'^events/assignments.ics$',
        views.event_assignments_ical,
        name='event_assignments_ical'),
    url(r'^events/$', views.events, name='events'),
    url(r'^events/data/$', views.events_data, name='events_data'),
    url(r'^events/redirect_thumbnail/(?P<id>\d+)/$',
        views.redirect_event_thumbnail,
        name='redirect_event_thumbnail'),
    url(r'^surveys/$', views.surveys_, name='surveys'),
    url(r'^surveys/new/$', views.survey_new, name='survey_new'),
    url(r'^surveys/(?P<id>\d+)/$', views.survey_edit, name='survey_edit'),
    url(r'^surveys/(?P<id>\d+)/delete/$', views.survey_delete,
        name='survey_delete'),
    url(r'^surveys/(?P<id>\d+)/question/(?P<question_id>\d+)/$',
        views.survey_question_edit,
        name='survey_question_edit'),
    url(r'^surveys/(?P<id>\d+)/question/(?P<question_id>\d+)/delete/$',
        views.survey_question_delete,
        name='survey_question_delete'),
    url(r'^surveys/(?P<id>\d+)/question/new/$',
        views.survey_question_new,
        name='survey_question_new'),

    url(r'^comments/$', views.all_comments, name='all_comments'),
    url(r'^comments/(?P<id>\d+)/$',
        views.comment_edit,
        name='comment_edit'),
    url(r'^events-autocomplete/$', views.event_autocomplete,
        name='event_autocomplete'),
    url(r'^participant-autocomplete/$', views.participant_autocomplete,
        name='participant_autocomplete'),
    url(r'^participants/new/$', views.participant_new, name='participant_new'),
    url(r'^participants/(?P<id>\d+)/$', views.participant_edit,
        name='participant_edit'),
    url(r'^participants/remove/(?P<id>\d+)/$', views.participant_remove,
        name='participant_remove'),
    url(r'^participants/email/(?P<id>\d+)/$', views.participant_email,
        name='participant_email'),
    url(r'^participants/$', views.participants, name='participants'),
    url(r'^channels/new/$', views.channel_new, name='channel_new'),
    url(r'^channels/(?P<id>\d+)/$', views.channel_edit,
        name='channel_edit'),
    url(r'^channels/remove/(?P<id>\d+)/$', views.channel_remove,
        name='channel_remove'),
    url(r'^channels/$', views.channels, name='channels'),
    url(r'^templates/env-autofill/$', views.template_env_autofill,
        name='template_env_autofill'),
    url(r'^templates/new/$', views.template_new, name='template_new'),
    url(r'^templates/(?P<id>\d+)/$', views.template_edit,
        name='template_edit'),
    url(r'^templates/remove/(?P<id>\d+)/$', views.template_remove,
        name='template_remove'),
    url(r'^templates/$', views.templates, name='templates'),
    url(r'^tags/$', views.tags, name='tags'),
    url(r'^tags/data/$', views.tags_data, name='tags_data'),
    url(r'^tags/(?P<id>\d+)/$', views.tag_edit, name='tag_edit'),
    url(r'^tags/remove/(?P<id>\d+)/$', views.tag_remove, name='tag_remove'),
    url(r'^tags/merge/(?P<id>\d+)/$', views.tag_merge, name='tag_merge'),
    url(r'^locations/new/$', views.location_new, name='location_new'),
    url(r'^locations/(?P<id>\d+)/$', views.location_edit,
        name='location_edit'),
    url(r'^locations/remove/(?P<id>\d+)/$', views.location_remove,
        name='location_remove'),
    url(r'^locations/tz/$', views.location_timezone, name='location_timezone'),
    url(r'^locations/$', views.locations, name='locations'),
    url(r'^approvals/$', views.approvals, name='approvals'),
    url(r'^approvals/reconsider/$', views.approval_reconsider,
        name='approval_reconsider'),
    url(r'^approvals/(?P<id>\d+)/$', views.approval_review,
        name='approval_review'),
    url(r'^pages/$', views.flatpages, name='flatpages'),
    url(r'^pages/new/$', views.flatpage_new, name='flatpage_new'),
    url(r'^pages/(?P<id>\d+)/$', views.flatpage_edit, name='flatpage_edit'),
    url(r'^pages/remove/(?P<id>\d+)/$', views.flatpage_remove,
        name='flatpage_remove'),
    url(r'^suggestions/$', views.suggestions, name='suggestions'),
    url(r'^suggestions/(?P<id>\d+)/$', views.suggestion_review,
        name='suggestion_review'),
    url(r'^vidly/$', views.vidly_media,
        name='vidly_media'),
    url(r'^vidly/status/$', views.vidly_media_status,
        name='vidly_media_status'),
    url(r'^vidly/info/$', views.vidly_media_info,
        name='vidly_media_info'),
    url(r'^vidly/resubmit/$', views.vidly_media_resubmit,
        name='vidly_media_resubmit'),
    url(r'^urltransforms/$', views.url_transforms,
        name='url_transforms'),
    url(r'^urltransforms/new/$', views.url_match_new,
        name='url_match_new'),
    url(r'^urltransforms/run/$', views.url_match_run,
        name='url_match_run'),
    url(r'^urltransforms/(?P<id>\d+)/remove/$', views.url_match_remove,
        name='url_match_remove'),
    url(r'^urltransforms/(?P<id>\d+)/add/$', views.url_transform_add,
        name='url_transform_add'),
    url(r'^urltransforms/(?P<id>\d+)/(?P<transform_id>\d+)/remove/$',
        views.url_transform_remove,
        name='url_transform_remove'),
    url(r'^urltransforms/(?P<id>\d+)/(?P<transform_id>\d+)/edit/$',
        views.url_transform_edit,
        name='url_transform_edit'),
    url(r'^cron-pings/$',
        views.cron_pings,
        name='cron_pings'),
    url(r'^curated-groups-autocomplete/',
        views.curated_groups_autocomplete,
        name='curated_groups_autocomplete'),
    url(r'^insufficient-permissions/',
        views.insufficient_permissions,
        name='insufficient_permissions'),
    url(r'^recruitmentmessages/$',
        views.recruitmentmessages,
        name='recruitmentmessages'),
    url(r'^recruitmentmessages/new/$',
        views.recruitmentmessage_new,
        name='recruitmentmessage_new'),
    url(r'^recruitmentmessages/(?P<id>\d+)/$',
        views.recruitmentmessage_edit,
        name='recruitmentmessage_edit'),
    url(r'^recruitmentmessages/(?P<id>\d+)/delete/$',
        views.recruitmentmessage_delete,
        name='recruitmentmessage_delete'),
    url(r'^loggedsearches/$',
        views.loggedsearches,
        name='loggedsearches'),
    url(r'^loggedsearches/stats/$',
        views.loggedsearches_stats,
        name='loggedsearches_stats'),
    url(r'^picturegallery/$',
        views.picturegallery,
        name='picturegallery'),
    url(r'^picturegallery/data/$',
        views.picturegallery_data,
        name='picturegallery_data'),
    url(r'^picturegallery/add/$',
        views.picture_add,
        name='picture_add'),
    url(r'^picturegallery/(?P<id>\d+)/$',
        views.picture_edit,
        name='picture_edit'),
    url(r'^picturegallery/(?P<id>\d+)/delete/$',
        views.picture_delete,
        name='picture_delete'),
    url(r'^picturegallery/(?P<id>\d+)/redirect_thumbnail/$',
        views.redirect_picture_thumbnail,
        name='redirect_picture_thumbnail'),
    url(r'^picturegallery/(?P<id>\d+)/event_associate/$',
        views.picture_event_associate,
        name='picture_event_associate'),
)
