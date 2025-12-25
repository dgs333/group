используй PostgreSQL и aiogram
plan:
1) сделать просто бота с апи гемини | сделано 70/30
2) добавить настройку конфига с базой данных
3) добавь чтобы он был как сглыпа
4) залить на норм хостинг/старый роутер | сделать на любом этапе 


message_id=6 date=datetime.datetime(2025, 12, 25, 16, 31, 30, tzinfo=TzInfo(0)) chat=Chat(id=8257115799, type='private', title=None, username='Mopsiks297', first_name='Mao', last_name=None, is_forum=None, is_direct_messages=None, accent_color_id=None, active_usernames=None, available_reactions=None, background_custom_emoji_id=None, bio=None, birthdate=None, business_intro=None, business_location=None, business_opening_hours=None, can_set_sticker_set=None, custom_emoji_sticker_set_name=None, description=None, emoji_status_custom_emoji_id=None, emoji_status_expiration_date=None, has_aggressive_anti_spam_enabled=None, has_hidden_members=None, has_private_forwards=None, has_protected_content=None, has_restricted_voice_and_video_messages=None, has_visible_history=None, invite_link=None, join_by_request=None, join_to_send_messages=None, linked_chat_id=None, location=None, message_auto_delete_time=None, permissions=None, personal_chat=None, photo=None, pinned_message=None, profile_accent_color_id=None, profile_background_custom_emoji_id=None, slow_mode_delay=None, sticker_set_name=None, unrestrict_boost_count=None) message_thread_id=None direct_messages_topic=None from_user=User(id=8257115799, is_bot=False, first_name='Mao', last_name=None, username='Mopsiks297', language_code='ru', is_premium=None, added_to_attachment_menu=None, can_join_groups=None, can_read_all_group_messages=None, supports_inline_queries=None, can_connect_to_business=None, has_main_web_app=None) sender_chat=None sender_boost_count=None sender_business_bot=None business_connection_id=None forward_origin=None is_topic_message=None is_automatic_forward=None reply_to_message=None external_reply=None quote=None reply_to_story=None reply_to_checklist_task_id=None via_bot=None edit_date=None has_protected_content=None is_from_offline=None is_paid_post=None media_group_id=None author_signature=None paid_star_count=None text='/gen fdgfd' entities=[MessageEntity(type='bot_command', offset=0, length=4, url=None, user=None, language=None, custom_emoji_id=None)] link_preview_options=None suggested_post_info=None effect_id=None animation=None audio=None document=None paid_media=None photo=None sticker=None story=None video=None video_note=None voice=None caption=None caption_entities=None show_caption_above_media=None has_media_spoiler=None checklist=None contact=None dice=None game=None poll=None venue=None location=None new_chat_members=None left_chat_member=None new_chat_title=None new_chat_photo=None delete_chat_photo=None group_chat_created=None supergroup_chat_created=None channel_chat_created=None message_auto_delete_timer_changed=None migrate_to_chat_id=None migrate_from_chat_id=None pinned_message=None invoice=None successful_payment=None refunded_payment=None users_shared=None chat_shared=None gift=None unique_gift=None connected_website=None write_access_allowed=None passport_data=None proximity_alert_triggered=None boost_added=None chat_background_set=None checklist_tasks_done=None checklist_tasks_added=None direct_message_price_changed=None forum_topic_created=None forum_topic_edited=None forum_topic_closed=None forum_topic_reopened=None general_forum_topic_hidden=None general_forum_topic_unhidden=None giveaway_created=None giveaway=None giveaway_winners=None giveaway_completed=None paid_message_price_changed=None suggested_post_approved=None suggested_post_approval_failed=None suggested_post_declined=None suggested_post_paid=None suggested_post_refunded=None video_chat_scheduled=None video_chat_started=None video_chat_ended=None video_chat_participants_invited=None web_app_data=None reply_markup=None forward_date=None forward_from=None forward_from_chat=None forward_from_message_id=None forward_sender_name=None forward_signature=None user_shared=None
Основные данные:
    message_id: 6
    date: 2025-12-25 16:31:30
    text: /gen fdgfd
Информация о чате (Chat):
    id: 8257115799
    type: private (личные сообщения)
    username: Mopsiks297
    first_name: Mao
Информация об отправителе (User):
    id: 8257115799
    is_bot: False
    language_code: ru
    is_premium: None (не указано)
Сущности (Entities) — то, что бот распознал в тексте:
    Тип: bot_command (/gen)
    Смещение (offset): 0
    Длина (length): 4
Остальные поля (пустые или по умолчанию):
    reply_to_message: None (это не ответ на другое сообщение)
    media: None (фото, видео или документов нет)
    forward_origin: None (сообщение не переслано)
    pinned_message: None

message_id=6 date=datetime.datetime(2025, 12, 25, 16, 31, 30, tzinfo=TzInfo(0))
chat=Chat( id=8257115799 type='private' username='Mopsiks297' first_name='Mao' )
from_user=User( id=8257115799 is_bot=False first_name='Mao' username='Mopsiks297' language_code='ru' )
text='/gen fdgfd'
entities=[MessageEntity( type='bot_command' offset=0 length=4 )]



Боты могут отправлять до 20 сообщений для чатов и каналов, до 30 сообщений в секунду. Этот лимит направлен на предотвращение спама и обеспечение устойчивости работы серверов.
Юзернейм бота — от 5 до 32 символов.
Описание — до 512 символов.
Информация о боте — до 120 символов.
Текстовое сообщение от бота не должно превышать 4096 символов.
Для описания медиафайлов — не более 1024.
Один отправленный файл не должен превышать 50МБ.
Бот может содержать до 100 команд, длина команды до 32 символов.











план базы данных
1) надо записывать все сообщения(промпты который ввели неиросети должно сохранять кто отправил промпт сам промпт)
2) сохранять все уникальные сообщения из чата группы от всех участников но не сохранять похожие типо оооо и оооооооо это два одинаковых
3) сохранять кастомные настройки апи гемини типо

1. Таблица ai_logs (Логирование промптов)
Здесь мы храним историю обращений к нейросети.
    id (SERIAL PRIMARY KEY): Уникальный номер записи.
    user_id (BIGINT): Telegram ID пользователя (из message.from_user.id).
    prompt (TEXT): Текст, который пользователь отправил нейросети.
    response (TEXT): Ответ, который вернула Gemini.
    mode (VARCHAR(20)): Название режима (например, 'short' или 'long').
    created_at (TIMESTAMP DEFAULT NOW()): Время запроса.

2. Таблица group_messages (Уникальные сообщения группы)
Для фильтрации похожих сообщений (типа "ооо" и "ооооо") мы будем использовать хэширование.
    id (SERIAL PRIMARY KEY): ID записи.
    chat_id (BIGINT): ID группы.
    user_id (BIGINT): Кто написал.
    content_hash (VARCHAR(64) UNIQUE): Уникальный ключ. Перед сохранением мы будем очищать текст от дублей букв и пробелов, делать из него хэш и записывать. Если хэш совпадет — база просто не примет запись.
    raw_text (TEXT): Оригинал сообщения.

3. Таблица ai_settings (Настройки режимов)
Вместо того чтобы прописывать настройки в коде, храним их здесь.
    mode_name (VARCHAR(20) PRIMARY KEY): Название ('short', 'unlimited').
    temperature (FLOAT): Креативность (0.0 - 1.0).
    max_tokens (INTEGER): Лимит длины.
    system_instruction (TEXT): Инструкция для модели.