export function getAllUsers() {
  return data.map((user) => ({
    id: user.id,
    name: user.name,
    city: user.city,
  }));
}

function findUser(predicate) {
  const users = data.filter(predicate);
  return users.length > 0 ? users.at(0) : null;
}

export function findUserByUsername(username) {
  return findUser((user) => user.username === username);
}

export function findUserById(userId) {
  return findUser((user) => user.id === userId);
}

export function findUserByCredentials(username, password) {
  return findUser((user) => user.username === username && user.password === password);
}

function getMaxId() {
  return data.length > 0 ? Math.max(...data.map((user) => user.id)) : 0;
}

export function createUser(userData) {
  let user = findUserByUsername(userData.username);
  if (user !== null) throw new Error(`Username ${userData.username} does already exist`);
  const maxId = getMaxId();
  data.push({
    id: maxId + 1,
    username: userData.username,
    password: userData.password,
    name: userData.name,
    city: userData.city,
  });
}

export function deleteUser(userId) {
  const index = data.findIndex((user) => user.id === userId);
  if (index >= 0) {
    data.splice(index, 1);
    return true;
  }
  return false;
}

const data = [
  { id: 1, username: "max", password: "debug", name: "Max Mustermann", city: "Berlin" },
  { id: 2, username: "alice", password: "qwertz", name: "Alice Wonderland", city: "Oz" },
  { id: 3, username: "bob", password: "1234", name: "Bob Ross", city: "Dallas" },
];
