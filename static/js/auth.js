axios.post('/api/token/', { username: 'example', password: 'password' })
    .then(response => {
        const token = response.data.access;
        saveToken(token); // Функція збереження токену з auth.js
        // Далі ви можете перенаправити користувача на іншу сторінку або оновити дані на поточній сторінці
    })
    .catch(error => console.error('Помилка отримання токену:', error));

axios.get('/api/protected-endpoint/', {
    headers: {
        Authorization: `Bearer ${getToken()}` // Функція отримання токену з auth.js
    }
})
.then(response => {
    console.log('Успішна відповідь:', response.data);
})
.catch(error => console.error('Помилка запиту до захищеного ендпоінту:', error));