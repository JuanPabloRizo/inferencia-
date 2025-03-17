def modus_tollens(q, p_implica_q):
    """Aplica Modus Tollens: si Q es falso y P → Q es verdadero, entonces P es falso."""
    if not q and p_implica_q:
        return False  # P es falso
    return True  # No se puede concluir que P es falso

# Si hay fuego (P), entonces hay humo (Q)
hay_humo = False  # Q es falso
implicacion = True  # P → Q

resultado = modus_tollens(hay_humo, implicacion)
print(f"¿Hay fuego? {resultado}")  # False
