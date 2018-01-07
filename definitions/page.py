definition = {
    'node_batch_size': 1,
    'fields': {
        'about': {'default': True},
        'access_token': {'omit': True},
        'ad_campaign': {'omit': True},
        'admin_notes': {'omit': True},
        'affiliation': {},
        'agencies': {'omit': True},
        'albums': {'edge_type': 'album'},
        'app_id': {'omit': True},
        'app_links': {'omit': True},
        'artists_we_like': {},
        'assigned_users': {'omit': True},
        'attire': {},
        'audio_copyrights': {'omit': True},
        'awards': {},
        'band_interests': {},
        'band_members': {},
        'bc_sponsored_posts': {'omit': True},
        'best_page': {},
        'bio': {},
        'birthday': {},
        'blocked': {'omit': True},
        'booking_agent': {},
        'broadcast_messages': {'omit': True},
        'built': {},
        'business': {'omit': True},
        'business_activities': {'omit': True},
        'businesssettinglogs': {'omit': True},
        'call_to_actions': {'omit': True},
        'can_checkin': {'omit': True},
        'can_post': {'omit': True},
        'canvas_elements': {'omit': True},
        'canvases': {'omit': True},
        'category': {'default': True},
        'category_list': {},
        'checkin_posts': {'omit': True},
        'checkins': {},
        'claimed_urls': {'omit': True},
        'company_overview': {},
        'connected_instagram_account': {'omit': True},
        'contact_address': {},
        'context': {'omit': True},
        'conversations': {'omit': True},
        'country_page_likes': {'omit': True},
        'cover': {},
        'culinary_team': {},
        'curated_collections': {'omit': True},
        'current_location': {},
        'description': {},
        'description_html': {},
        'directed_by': {},
        'display_subtext': {},
        'displayed_message_response_time': {'omit': True},
        'emails': {},
        'engagement': {},
        'events': {'edge_type': 'event'},
        'fan_count': {},
        'featured_video': {'edge_type': 'video'},
        'featured_videos_collection': {'omit': True},
        'features': {},
        'feed': {'edge_type': 'post'},
        'food_styles': {},
        'founded': {},
        'general_info': {},
        'general_manager': {},
        'genre': {},
        'global_brand_children': {'omit': True},
        'global_brand_page_name': {'omit': True},
        'global_brand_root_id': {'omit': True},
        'has_added_app': {'omit': True},
        'has_whatsapp_number': {'omit': True},
        'hometown': {},
        'hours': {},
        'impressum': {},
        'influences': {},
        'insights': {'omit': True},
        'instagram_business_account': {'omit': True},
        'instant_articles': {'omit': True},
        'instant_articles_insights': {'omit': True},
        'instant_articles_review_status': {'omit': True},
        'is_always_open': {},
        'is_chain': {},
        'is_community_page': {},
        'is_eligible_for_branded_content': {'omit': True},
        'is_owned': {},
        'is_permanently_closed': {},
        'is_published': {'omit': True},
        'is_unclaimed': {'omit': True},
        'is_verified': {'omit': True},
        'is_webhooks_subscribed': {'omit': True},
        'labels': {'omit': True},
        'leadgen_conditional_questions_group': {'omit': True},
        'leadgen_context_cards': {'omit': True},
        'leadgen_draft_forms': {'omit': True},
        'leadgen_form_preview_details': {'omit': True},
        'leadgen_forms': {'omit': True},
        'leadgen_has_crm_integration': {'omit': True},
        'leadgen_has_fat_ping_crm_integration': {'omit': True},
        'leadgen_legal_content': {'omit': True},
        'leadgen_qualifiers': {'omit': True},
        'leadgen_tos_acceptance_time': {'omit': True},
        'leadgen_tos_accepted': {'omit': True},
        'leadgen_tos_accepting_user': {'omit': True},
        'leadgen_whitelisted_users': {'omit': True},
        'likes': {'edge_type': 'page', 'follow_edge': False},
        'link': {'default': True},
        'live_encoders': {'omit': True},
        'live_videos': {'edge_type': 'livevideo'},
        'location': {},
        'locations': {'omit': True},
        'media_fingerprints': {'omit': True},
        'members': {},
        'merchant_id': {'omit': True},
        'merchant_review_status': {'omit': True},
        'messenger_ads_quick_replies_type': {'omit': True},
        'messenger_profile': {'omit': True},
        'milestones': {'omit': True},
        'mission': {},
        'mpg': {},
        'name': {'default': True},
        'name_with_location_descriptor': {},
        'nativeoffers': {'omit': True},
        'network': {},
        'new_like_count': {'omit': True},
        'notes': {'omit': True},
        'notifications': {'omit': True},
        'offer_eligible': {'omit': True},
        'offers_v3': {'omit': True},
        'overall_star_rating': {},
        'page_token': {'omit': True},
        'parent_page': {'edge_type': 'page', 'follow_edge': False},
        'parking': {},
        'payment_options': {},
        'pending_users': {'omit': True},
        'personal_info': {},
        'personal_interests': {},
        'pharma_safety_info': {},
        'phone': {},
        'photos': {'edge_type': 'photo'},
        'picture': {},
        'place_topics': {},
        'place_type': {},
        'plot_outline': {},
        'posts': {'omit': True},
        'preferred_audience': {'omit': True},
        'press_contact': {},
        'price_range': {},
        'produced_by': {},
        'product_catalogs': {'omit': True},
        'products': {},
        'promotable_posts': {'omit': True},
        'promotion_eligible': {'omit': True},
        'promotion_ineligible_reason': {'omit': True},
        'public_transit': {},
        'publisher_space': {'omit': True},
        'questions': {'omit': True},
        'rating_count': {},
        'ratings': {'omit': True},
        'recipient': {'omit': True},
        'record_label': {},
        'release_date': {},
        'restaurant_orders': {'omit': True},
        'restaurant_services': {'omit': True},
        'restaurant_specialties': {'omit': True},
        'roles': {'omit': True},
        'rtb_dynamic_posts': {'omit': True},
        'saved_filters': {'omit': True},
        'saved_message_responses': {'omit': True},
        'schedule': {},
        'scheduled_posts': {'omit': True},
        'screennames': {},
        'screenplay_by': {},
        'season': {},
        'seasons': {},
        'secondary_receivers': {'omit': True},
        'settings': {'omit': True},
        'show_playlists': {},
        'single_line_address': {},
        'starring': {},
        'start_info': {},
        'store_location_descriptor': {},
        'store_number': {},
        'studio': {},
        'subscribed_apps': {'omit': True},
        'supports_instant_articles': {'omit': True},
        'tabs': {'omit': True},
        'tagged': {'omit': True},
        'talking_about_count': {},
        'thread_settings': {'omit': True},
        'threads': {'omit': True},
        'tours': {},
        'unread_message_count': {'omit': True},
        'unread_notif_count': {'omit': True},
        'unseen_message_count': {'omit': True},
        'username': {'default': True},
        'verification_status': {},
        'video_broadcasts': {'omit': True},
        'video_copyright_rules': {'omit': True},
        'video_copyrights': {'omit': True},
        'video_lists': {'omit': True},
        'video_media_copyrights': {'omit': True},
        'videos': {'edge_type': 'video'},
        'videos_you_can_use': {'omit': True},
        # Example: SenatorTedCruz
        'visitor_posts': {'edge_type': 'post', 'omit_on_error': True},
        'voip_info': {'omit': True},
        'website': {'default': True},
        'were_here_count': {'omit': True},
        'whatsapp_number': {},
        'workflows': {'omit': True},
        'written_by': {},
    }
}

