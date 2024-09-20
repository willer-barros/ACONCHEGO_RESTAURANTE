import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Order() {
    const [menuItems, setMenuItems] = useState([]);
    const [selectedItem, setSelectedItem] = useState(null);

    useEffect(() => {
        const fetchMenuItems = async () => {
            const response = await axios.get('http://localhost:8000/menu/');
            setMenuItems(response.data);
        };
        fetchMenuItems();
    }, []);

    const handleOrder = async () => {
        const token = localStorage.getItem('access_token');
        try {
            await axios.post(
                'http://localhost:8000/orders/',
                { items: [selectedItem] },
                {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                }
            );
            alert('Pedido feito com sucesso!');
        } catch (error) {
            console.error("Erro ao fazer o pedido", error);
        }
    };

    return (
        <div>
            <h1>Faça seu pedido</h1>
            <select onChange={(e) => setSelectedItem(e.target.value)}>
                <option value="">Escolha um item</option>
                {menuItems.map((item) => (
                    <option key={item.id} value={item.id}>
                        {item.name}
                    </option>
                ))}
            </select>
            <button onClick={handleOrder}>Enviar Pedido</button>
        </div>
    );
}

export default Order;
