CREATE TABLE IF NOT EXISTS users (
  id int,
  login varchar(255),
  money_amount int,
  card_number varchar(16),
  status int
);

CREATE TABLE IF NOT EXISTS  password (
  id int,
  password varchar(255)
);

INSERT INTO users
VALUES (1, 'admin', 0, '4103424051263531', 1);
INSERT INTO password
VALUES (1, 'admin');

INSERT INTO users
VALUES (2, 'Harry Potter', 520900, '5527182603772285', 1);
INSERT INTO password
VALUES (2, 'wlkwe2_23');

INSERT INTO users
VALUES (3, 'Hermione Granger', 23890, '5155884019963304', 1);
INSERT INTO password
VALUES (3, '1234876sfjkbw');

INSERT INTO users
VALUES (4, 'Ronald Weasley', 10, '379074029512652', 1);
INSERT INTO password
VALUES (4, '2bl3lb42');

INSERT INTO users
VALUES (5, 'Neville Longbottom', 107020, '6011784786181787', 0);
INSERT INTO password
VALUES (5, '1c2jkvhl');

INSERT INTO users
VALUES (6, 'Albus Dumbledore', 987654456, '4916767351457220', 0);
INSERT INTO password
VALUES (6, 'qwertyuiop12345');
