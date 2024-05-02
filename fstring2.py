#Formatação de Strings com várias linhas
escola = 'Senai'
curso = 'Desenvolvimento de Sistemas'
uc = 'Lógica de Programação'
matricula = 34
nota = 9.99999
print(f"Escola: {escola}\n"
      f"Curso: {curso}\n"
      f"Unidade Curricular: {uc}\n"
      f"Matrícula: {matricula:06d}\n"
      f"nota: {nota:.2f}")