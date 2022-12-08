from model.models import Colaboradores,Departamentos,Dependentes,Projetos,Pesquisador,Limpeza,Supervisor, Secretario,Horastrabalho

dep = Departamentos()
print(dep.save())

colab = Colaboradores()
print(colab.save())

depen = Dependentes()
print(depen.save())

horas = Horastrabalho()
print(horas.save())

proj = Projetos()
print(proj.save())

sup = Supervisor()
print(sup.save())

lim = Limpeza()
print(lim.save())

pesq = Pesquisador()
print(pesq.save())

sec = Secretario()
print(sec.save())
