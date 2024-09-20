import React, { useState } from 'react';
import axios from 'axios';

function Login(){
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try{
            const response = await axios.post('http://localhost:8000/token/', {
                username,
                password,
            });

            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
            alert('Login Realizado');
        
        } catch(error){
        console.error('Login invalido', error);
        alert("Credenciais Invalidas")
        }
    }

    return(
        <form onSubmit={handleSubmit}>
            <input
            type='text'
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder='Login'
            />
    
            <input
            type='password'
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder='Senha'
            />

            <button type='submit'>Login</button>
        </form>
    );
}

export default Login;