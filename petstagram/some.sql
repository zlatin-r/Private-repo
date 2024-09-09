SELECT "django_session".
           "session_key",
       "django_session".
           "session_data",
       "django_session".
           "expire_date"
FROM "django_session"
WHERE ("django_session".
           "expire_date" > '2024-09-09 17:56:27.124492'
    AND
       "django_session".
           "session_key" = 'l2edmujrw5oqfc5uj6xq4xiaooy9tb7p') LIMIT
21;
args
= ('2024-09-09 17:56:27.124492', 'l2edmujrw5oqfc5uj6xq4xiaooy9tb7p');
alias
= default

SELECT "auth_user".
           "id",
       "auth_user".
           "password",
       "auth_user".
           "last_login",
       "auth_user".
           "is_superuser",
       "auth_user".
           "username",
       "auth_user".
           "first_name",
       "auth_user".
           "last_name",
       "auth_user".
           "email",
       "auth_user".
           "is_staff",
       "auth_user".
           "is_active",
       "auth_user".
           "date_joined"
FROM "auth_user"
WHERE "auth_user".
          "id" = 1 LIMIT
21;
args
= (1,);
alias
= default

SELECT "photos_photo".
           "id",
       "photos_photo".
           "photo",
       "photos_photo".
           "description",
       "photos_photo".
           "location",
       "photos_photo".
           "date_of_publication"
FROM "photos_photo";
args
= ();
alias
= default

SELECT COUNT(*)
           AS
           "__count"
FROM "common_photolike"
WHERE "common_photolike".
          "pet_photo_id" = 6;
args
= (6,);
alias
= default

SELECT COUNT(*)
           AS
           "__count"
FROM "common_photolike"
WHERE "common_photolike".
          "pet_photo_id" = 6;
args
= (6,);
alias
= default

SELECT "pets_pet".
           "id",
       "pets_pet".
           "name",
       "pets_pet".
           "pet_photo",
       "pets_pet".
           "date_of_birth",
       "pets_pet".
           "slug"
FROM "pets_pet"
         INNER JOIN
     "photos_photo_tagged_pets"
     ON ("pets_pet".
             "id" = "photos_photo_tagged_pets".
             "pet_id")
WHERE "photos_photo_tagged_pets".
          "photo_id" = 6;
args
= (6,);
alias
= default
