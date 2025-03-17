def modus_ponens(p, p_implica_q):
    """Aplica Modus Ponens: si P es verdadero y P → Q es verdadero, entonces Q es verdadero."""
    if p and p_implica_q:
        return True  # Q es verdadero
    return False  # No se puede concluir Q

# Si estudias (P), entonces apruebas (Q)
estudias = True  # P
implicacion = True  # P → Q

resultado = modus_ponens(estudias, implicacion)
print(f"¿Aprobarás el examen? {resultado}")  # True
