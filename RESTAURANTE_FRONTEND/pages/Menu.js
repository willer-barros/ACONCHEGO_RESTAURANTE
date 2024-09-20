import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Menu() {
    const [menuItems, setMenuItems] = useState([]);

    useEffect(() => {
        const fetchMenuItems = async () => {
            const response = await axios.get('http://localhost:8000/menu/');
            setMenuItems(response.data);
        };
        fetchMenuItems();
    }, []);

    return (
        <div>
            <h1>Menu</h1>
            <ul>
                {menuItems.map((item) => (
                    <li key={item.id}>
                        {item.name} - ${item.price}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Menu;
