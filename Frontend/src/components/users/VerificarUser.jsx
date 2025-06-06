import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./css/Verificar.css";

function VerificarUser() {
  const [email, setEmail] = useState("");
  const [code, setCode] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch("http://127.0.0.1:8000/active_user", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, code }),
    });

    const data = await response.json();

    if (response.status === 200) {
      alert("✅ Usuário ativado com sucesso!");
      navigate("/login", { state: { email } });
    } else if (response.status === 401) {
      alert("⚠️ Usuário já está ativado.");
      navigate("/login", { state: { email } });
    } else {
      alert("❌ Erro: " + (data.ERRO || data.erro || "Código incorreto"));
    }
  };

  return (
    <div id="verificar-container">
      <h1>Verificar Código</h1>
      <form className="verificar-form" onSubmit={handleSubmit}>
        <label>
          Email:
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        <label>
          Código:
          <input
            type="text"
            value={code}
            onChange={(e) => setCode(e.target.value)}
            required
          />
        </label>
        <button type="submit">Verificar</button>
      </form>
    </div>
  );
}

export default VerificarUser;
