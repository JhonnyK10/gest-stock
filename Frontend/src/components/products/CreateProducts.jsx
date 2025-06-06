import React, { useState } from "react";
import axios from "axios";
import "./css/CreateProducts.css"; 

function NewProduct() {
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");
  const [quantity, setQuantity] = useState("");
  const [imagem, setImagem] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const token = sessionStorage.getItem("token"); // ajustado aqui
    if (!token) {
      setMessage("Usuário não autenticado.");
      return;
    }

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/new_product",
        {
          name,
          price: parseFloat(price),
          quantity: parseInt(quantity),
          imagem,
        },
        {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
        }
      );

      setMessage(response.data.mensagem);
      setName("");
      setPrice("");
      setQuantity("");
      setImagem("");
    } catch (error) {
      if (error.response) {
        setMessage(error.response.data.erro);
      } else {
        setMessage("Erro ao enviar o formulário");
      }
    }
  };

  return (
    <>
      <header>
        {" "}
        <h1 className="site-name">Gest Stock</h1>
        <div className="btn-container">
          <a href="/store_products">
            <button className="btn">Loja</button>
          </a>
          <a href="/user_purchases">
            <button className="btn">Minhas Compras</button>
          </a>
          <a href="/user_sales">
            <button className="btn">Minhas Vendas</button>
          </a>
          <a href="/user_products">
            <button className="btn">Meus Produtos</button>
          </a>
        </div>
      </header>

      <div id="createP-container">
        <h1>Cadastrar <br /> Novo Produto</h1>
        <form className="createP-form" onSubmit={handleSubmit}>
          <div>
            <label>Nome:</label>
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
            />
          </div>

          <div>
            <label>Preço:</label>
            <input
              type="number"
              step="0.01"
              value={price}
              onChange={(e) => setPrice(e.target.value)}
              required
            />
          </div>

          <div>
            <label>Quantidade:</label>
            <input
              type="number"
              value={quantity}
              onChange={(e) => setQuantity(e.target.value)}
              required
            />
          </div>

          <div>
            <label>Imagem (URL):</label>
            <input
              type="text"
              value={imagem}
              onChange={(e) => setImagem(e.target.value)}
            />
          </div>

          <button type="submit">Cadastrar Produto</button>
        </form>

        {message && <p>{message}</p>}
      </div>
    </>
  );
}

export default NewProduct;
