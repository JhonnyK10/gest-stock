import React from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import CadastroUser from "./components/users/CadastroUser.jsx";
import LoginUser from "./components/users/LoginUser.jsx";
import VerificarUser from "./components/users/VerificarUser.jsx";
import UserPurchases from "./components/products/UserPurchases.jsx";
import UserProducts from "./components/products/UserProducts.jsx";
import StoreProducts from "./components/products/StoreProducts.jsx";
import NewProduct from "./components/products/CreateProducts.jsx";
import UserSales from "./components/products/UserSales.jsx";

createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />}>
          {" "}
        </Route>
        <Route path="/cadastro" element={<CadastroUser />}>
          {" "}
        </Route>
        <Route path="/adicionar-produto" element={<NewProduct />}>
          {" "}
        </Route>
        <Route path="/login" element={<LoginUser />}>
          {" "}
        </Route>
        <Route path="/verificar" element={<VerificarUser />}>
          {" "}
        </Route>
        <Route path="/user_purchases" element={<UserPurchases />}>
          {" "}
        </Route>
        <Route path="/user_products" element={<UserProducts />}>
          {" "}
        </Route>
        <Route path="/user_sales" element={<UserSales />}>
          {" "}
        </Route>
        <Route path="/store_products" element={<StoreProducts />}>
          {" "}
        </Route>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
