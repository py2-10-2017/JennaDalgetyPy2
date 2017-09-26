SELECT users.id, users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name
FROM friendships.users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id;
-- INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
-- VALUES (4, 1, NOW(), NOW())