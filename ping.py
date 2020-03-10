import os 
contador = 0
for h in range(1, 255, 1):
    if os.system("ping 200.33.171."+str(h)) == 0:
        contador +=1
        print(" ->SÍ está activa")
    else:
        print(" -> NO está activa")

print("Total activas: " + str(contador) + "\n Total inactivas: " + str(255-contador))

""" RESULTADO
Haciendo ping a 200.33.171.163 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.163:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.164 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.164:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.165 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.165:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.166 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.166:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.167 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.167:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.168 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.168:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.169 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.169:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.170 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.170:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.171 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.171:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.172 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.172:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.173 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.173:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.174 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.174:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.175 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.175:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.176 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.176:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.177 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.177:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.178 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.178:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.179 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.179:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.180 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.180:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.181 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.181:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.182 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.182:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.183 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.183:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.184 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.184:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.185 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.185:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.186 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.186:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.187 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.187:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.188 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.188:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.189 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.189:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.190 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.190:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.191 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.191:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.192 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.192:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.193 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.193:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.194 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.194:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.195 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.195:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.196 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.196:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.197 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.197:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.198 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.198:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.199 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.199:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.200 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.200:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.201 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.201:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.202 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.202:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.203 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.203:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.204 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.204:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.205 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.205:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.206 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.206:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.207 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.207:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.208 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.208:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.209 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.209:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.210 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.210:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.211 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.211:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.212 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.212:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.213 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.213:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.214 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.214:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.215 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.215:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.216 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.216:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.217 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.217:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.218 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.218:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.219 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.219:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.220 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.220:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.221 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.221:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.222 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.222:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.223 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.223:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.224 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.224:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.225 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.225:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.226 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.226:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.227 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.227:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.228 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.228:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.229 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.229:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.230 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.230:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.231 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.231:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.232 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.232:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.233 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.233:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.234 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.234:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.235 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.235:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.236 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.236:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.237 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.237:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.238 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.238:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.239 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.239:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.240 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.240:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.241 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.241:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.242 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.242:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.243 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.243:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.244 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.244:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.245 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.245:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.246 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.246:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.247 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.247:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.248 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.248:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.249 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.249:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.250 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.250:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.251 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.251:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.252 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.252:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.253 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 200.33.171.253:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
 -> NO está activa

Haciendo ping a 200.33.171.254 con 32 bytes de datos:
Respuesta desde 200.33.171.254: bytes=32 tiempo=97ms TTL=242
Respuesta desde 200.33.171.254: bytes=32 tiempo=33ms TTL=242
Respuesta desde 200.33.171.254: bytes=32 tiempo=74ms TTL=242
Respuesta desde 200.33.171.254: bytes=32 tiempo=338ms TTL=242

Estadísticas de ping para 200.33.171.254:
    Paquetes: enviados = 4, recibidos = 4, perdidos = 0
    (0% perdidos),
Tiempos aproximados de ida y vuelta en milisegundos:
    Mínimo = 33ms, Máximo = 338ms, Media = 135ms
 ->SÍ está activa
Total activas: 16
 Total inactivas: 239
"""