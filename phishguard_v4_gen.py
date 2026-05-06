#!/usr/bin/env python3
"""
PhishGuard v4.0 – Generador de código
Genera PhishGuard_v4.html en el directorio actual.
Uso:  python phishguard_v4_gen.py
"""
import json
from pathlib import Path

# ══════════════════════════════════════════════════════════
#  DATOS: 26 ESCENARIOS DE EMAIL
# ══════════════════════════════════════════════════════════
EMAILS = [
# ── NIVEL 1: AMENAZAS BÁSICAS ─────────────────────────────
{
  "id":1,"level":1,"isPhishing":True,
  "from_name":"Soporte Banco Nacional","from_email":"soporte@banconacional-seguridad.xyz",
  "to":"empleado@miempresa.com","date":"Hoy, 09:14 AM",
  "subject":"⚠️ URGENTE: Su cuenta ha sido SUSPENDIDA – Actúe AHORA",
  "body_html":'<div class="em-header" style="background:#003087">🏦 BANCO NACIONAL – Seguridad</div><div class="em-body"><p>Estimado cliente,</p><p><strong style="color:#cc0000">⚠️ SU CUENTA HA SIDO SUSPENDIDA TEMPORALMENTE</strong></p><p>Hemos detectado actividad <strong>SOSPECHOSA</strong>. Debe verificar en las próximas <strong style="color:#cc0000">2 HORAS</strong> o su cuenta será <u>cerrada permanentemente</u>.</p><div class="em-cta-wrap"><a class="em-cta" href="#" style="background:#003087">🔓 VERIFICAR MI CUENTA AHORA</a></div><p>Necesitará: número de cuenta, contraseña, tarjeta y CVV.</p><p class="em-footer">Si no actúa, su cuenta será eliminada. Este es su único aviso.</p></div>',
  "red_flags":[
    {"icon":"🌐","title":"Dominio falso (.xyz)","desc":"Los bancos nunca usan extensiones .xyz. El dominio real es verificable en la web oficial."},
    {"icon":"⏰","title":"Urgencia artificial","desc":"'2 HORAS' es manipulación psicológica. Los bancos reales notifican con días de antelación."},
    {"icon":"🔑","title":"Solicitud de datos críticos","desc":"Ningún banco legítimo pide contraseña y CVV por correo. Siempre es trampa."},
    {"icon":"📢","title":"MAYÚSCULAS y amenazas","desc":"Uso de mayúsculas, exclamaciones y amenazas de cierre son ingeniería social clásica."},
  ],
  "explanation":"Phishing bancario clásico. Dominio falso + urgencia + datos sensibles. Los bancos reales NUNCA piden CVV por email.",
  "legit_reason":None,"points":100,"time_limit":30,
},
{
  "id":2,"level":1,"isPhishing":False,
  "from_name":"IT Support – MiEmpresa","from_email":"soporte.ti@miempresa.com",
  "to":"empleado@miempresa.com","date":"Hoy, 10:30 AM",
  "subject":"Mantenimiento programado de sistemas – Sábado 02:00–04:00 AM",
  "body_html":'<div class="em-header" style="background:#1a237e">💻 Departamento de TI – MiEmpresa</div><div class="em-body"><p>Estimado equipo,</p><p>El próximo <strong>sábado 15 de junio</strong> realizaremos mantenimiento preventivo.</p><p><strong>Horario:</strong> 02:00 AM – 04:00 AM</p><ul><li>Correo electrónico corporativo</li><li>VPN corporativa</li><li>Intranet y recursos compartidos</li></ul><p>No es necesario realizar ninguna acción. Para consultas: <strong>ext. 2200</strong>.</p><p><strong>Equipo de TI</strong> | soporte.ti@miempresa.com</p></div>',
  "red_flags":[],"explanation":"Correo legítimo de TI. Dominio corporativo oficial, sin datos sensibles, canales verificables.",
  "legit_reason":"Dominio corporativo oficial · Sin solicitud de credenciales · Canales internos verificables",
  "points":100,"time_limit":30,
},
{
  "id":3,"level":1,"isPhishing":True,
  "from_name":"Amazon","from_email":"noreply@amazon-confirmaciones-pedidos.net",
  "to":"empleado@miempresa.com","date":"Ayer, 11:45 PM",
  "subject":"Pedido #AMZ-8847291 – Confirme su dirección URGENTE",
  "body_html":'<div class="em-header" style="background:#ff9900;color:#232f3e">📦 amazon – Confirmación de Pedido</div><div class="em-body"><p>Hemos procesado su pedido pero necesitamos confirmar su dirección de entrega.</p><div class="em-info-box" style="border-color:#ff9900;background:#fff8ee"><strong>Pedido #AMZ-8847291</strong><br>iPhone 15 Pro Max 256GB | Total: $1,299.99 USD<br>Estado: <span style="color:#e67e00">⚠️ Pendiente de confirmación</span></div><p><strong>Si no confirma en 24 horas, el pedido será cancelado y se realizará el cargo de todas formas.</strong></p><div class="em-cta-wrap"><a class="em-cta" href="#" style="background:#ff9900;color:#232f3e">Confirmar Dirección y Datos de Pago</a></div><p class="em-footer">Amazon.com © 2024</p></div>',
  "red_flags":[
    {"icon":"🌐","title":"Dominio impostor","desc":"Amazon usa amazon.com. 'amazon-confirmaciones-pedidos.net' es un dominio de atacantes."},
    {"icon":"🛒","title":"Pedido no solicitado","desc":"El atacante espera que hagas clic para 'cancelarlo'. Ambas opciones capturan credenciales."},
    {"icon":"💳","title":"Solicitud de datos de pago","desc":"Amazon nunca pide datos de pago por email para pedidos ya procesados."},
    {"icon":"⚠️","title":"Contradicción lógica","desc":"'Cancelado pero con cargo de todas formas' es amenaza ilógica diseñada para generar pánico."},
  ],
  "explanation":"Phishing de Amazon con pedido falso de alto valor. Objetivo: robar credenciales mientras intentas 'cancelar' el cargo.",
  "legit_reason":None,"points":100,"time_limit":30,
},
{
  "id":4,"level":1,"isPhishing":False,
  "from_name":"María González – RRHH","from_email":"m.gonzalez@miempresa.com",
  "to":"empleado@miempresa.com","date":"Hoy, 08:15 AM",
  "subject":"Recordatorio: Encuesta de Clima Laboral 2024 – Vence el viernes",
  "body_html":'<div class="em-header" style="background:#2e7d32">👥 Recursos Humanos – MiEmpresa</div><div class="em-body"><p>Estimado colaborador,</p><p>Le recordamos que la <strong>Encuesta Anual de Clima Laboral 2024</strong> cierra el próximo <strong>viernes 19 de junio</strong>.</p><p>La encuesta es completamente <strong>anónima</strong> y toma aproximadamente 10 minutos.</p><div class="em-info-box" style="border-color:#2e7d32;background:#f1f8e9"><strong>Acceso:</strong> Intranet → Recursos Humanos → Encuesta Clima 2024</div><p>El <strong>67% del equipo</strong> ya ha participado.<br><strong>María González</strong> – Analista RRHH | Ext. 1045</p></div>',
  "red_flags":[],"explanation":"Correo legítimo de RRHH. Dominio corporativo, sin credenciales, acceso vía intranet, contacto verificable.",
  "legit_reason":"Dominio corporativo · Acceso solo por intranet · Sin datos sensibles · Contacto interno verificable",
  "points":100,"time_limit":30,
},
# ── NIVEL 2: NIVEL INTERMEDIO ─────────────────────────────
{
  "id":5,"level":2,"isPhishing":True,
  "from_name":"IT Helpdesk Corporativo","from_email":"helpdesk@miempresa-support.com",
  "to":"empleado@miempresa.com","date":"Hoy, 07:58 AM",
  "subject":"Acción requerida: Su contraseña corporativa expira en 24 horas",
  "body_html":'<div class="em-header" style="background:#37474f">🔐 IT Helpdesk – Seguridad Corporativa</div><div class="em-body"><p>Estimado empleado,</p><p>Nuestros sistemas detectaron que su contraseña corporativa <strong>expirará en 24 horas</strong>. Sin acción, perderá acceso a <u>todos</u> los sistemas.</p><div class="em-info-box" style="border-color:#ff9800;background:#fff3e0">⚠️ <strong>Acción requerida antes de:</strong> Mañana 08:00 AM</div><p>Ingrese sus credenciales actuales y defina una nueva contraseña:</p><div class="em-cta-wrap"><a class="em-cta" href="#" style="background:#37474f">🔑 Actualizar Contraseña Ahora</a></div><p class="em-footer">IT Security Team | No responda a este correo</p></div>',
  "red_flags":[
    {"icon":"🌐","title":"Typosquatting (dominio casi idéntico)","desc":"'miempresa-support.com' vs 'miempresa.com'. Verifica siempre el dominio exacto."},
    {"icon":"🔑","title":"Trampa de credenciales","desc":"El portal pedirá tu contraseña ACTUAL. IT real nunca necesita tu clave vigente para un reset."},
    {"icon":"⏰","title":"Urgencia de 24h fabricada","desc":"Las políticas de expiración se notifican con varios días y desde el propio sistema operativo."},
    {"icon":"📧","title":"'Estimado empleado' sin nombre","desc":"Un sistema corporativo real conoce tu nombre. El saludo genérico indica campaña masiva."},
  ],
  "explanation":"Phishing de credenciales que imita al IT. Typosquatting sutil + urgencia. Objetivo: robar tu contraseña corporativa.",
  "legit_reason":None,"points":150,"time_limit":25,
},
{
  "id":6,"level":2,"isPhishing":False,
  "from_name":"Facturación – Proveedor ABC","from_email":"facturas@proveedorabc.com",
  "to":"empleado@miempresa.com","date":"Ayer, 04:22 PM",
  "subject":"Factura #FAC-2024-0445 – Servicios de Consultoría Junio 2024",
  "body_html":'<div class="em-header" style="background:#1565c0">📄 Proveedor ABC S.A. – Facturación</div><div class="em-body"><p>Estimado equipo de MiEmpresa,</p><p>Adjuntamos la factura de servicios de junio 2024, según contrato <strong>#CM-2023-089</strong>.</p><div class="em-info-box" style="border-color:#1565c0;background:#e3f2fd">Número: <strong>FAC-2024-0445</strong> | Período: 01/06/2024 – 30/06/2024<br>Concepto: Consultoría en gestión de proyectos<br>Monto: $4,500.00 + IVA | Vencimiento: 30/07/2024</div><p>Para consultas: facturas@proveedorabc.com | Tel: +1 (555) 234-5678</p><p><strong>Dept. de Facturación</strong> – Proveedor ABC S.A.</p></div>',
  "red_flags":[],"explanation":"Factura legítima. Referencia a contrato específico, múltiples canales verificables, sin urgencia.",
  "legit_reason":"Referencia a contrato existente · Sin urgencia · Múltiples canales verificables · Sin solicitud de credenciales",
  "points":150,"time_limit":25,
},
{
  "id":7,"level":2,"isPhishing":True,
  "from_name":"Microsoft 365 Security","from_email":"security-alert@microsoft365-secure-team.com",
  "to":"empleado@miempresa.com","date":"Hoy, 06:33 AM",
  "subject":"Alerta: Inicio de sesión desde ubicación desconocida – Moscú, Rusia",
  "body_html":'<div class="em-header" style="background:#0078d4">🪟 Microsoft 365 Security Alert</div><div class="em-body"><p>Detectamos un inicio de sesión inusual en su cuenta:</p><div class="em-info-box" style="border-color:#ffc107;background:#fff3cd">📍 <strong>Ubicación:</strong> Moscú, Rusia<br>🕐 <strong>Hora:</strong> 06:28 AM (hace 5 minutos)<br>💻 <strong>Dispositivo:</strong> Windows PC desconocido</div><p>Si no fue usted, tome acción <strong>inmediata</strong>:</p><div class="em-cta-wrap"><a class="em-cta" href="#" style="background:#d32f2f;margin-right:8px">🔒 Asegurar mi Cuenta</a><a class="em-cta" href="#" style="background:#0078d4">✅ Fui Yo</a></div><p class="em-footer">Microsoft Corporation © 2024</p></div>',
  "red_flags":[
    {"icon":"🌐","title":"Dominio Microsoft falso","desc":"Microsoft envía desde microsoft.com. 'microsoft365-secure-team.com' es un dominio impostor."},
    {"icon":"🗺️","title":"Geografía alarmante calculada","desc":"Usar 'Moscú, Rusia' maximiza el pánico. Los atacantes eligen ubicaciones que generan reacción inmediata."},
    {"icon":"🎯","title":"Dos botones = trampa doble","desc":"Ambos botones ('Asegurar' y 'Fui Yo') llevan al mismo sitio de phishing."},
    {"icon":"⏱️","title":"'Hace 5 minutos': presión extrema","desc":"La precisión temporal crea urgencia máxima. Es un dato inventado para impedir análisis."},
  ],
  "explanation":"Phishing de credenciales Microsoft. Con tu acceso M365 el atacante obtiene correo, OneDrive, Teams y todos los servicios.",
  "legit_reason":None,"points":150,"time_limit":25,
},
{
  "id":8,"level":2,"isPhishing":False,
  "from_name":"Carlos Mendoza – Gerente General","from_email":"c.mendoza@miempresa.com",
  "to":"empleado@miempresa.com","date":"Hoy, 09:45 AM",
  "subject":"Reunión de equipo – Resultados Q2 y planificación Q3",
  "body_html":'<div class="em-header" style="background:#4a148c">📅 Comunicación Interna – Gerencia General</div><div class="em-body"><p>Hola equipo,</p><p>Los convoco a la <strong>reunión mensual de resultados</strong> Q2 y planificación Q3 2024.</p><div class="em-info-box" style="border-color:#4a148c;background:#f3e5f5">📅 <strong>Fecha:</strong> Jueves 20 de junio, 10:00 AM – 12:00 PM<br>📍 <strong>Lugar:</strong> Sala de Conferencias A (piso 3) + Teams</div><p><strong>Agenda:</strong> KPIs Q2 · Análisis de brechas · Objetivos Q3 · Preguntas</p><p>Confirmen asistencia respondiendo este correo.<br><strong>Carlos Mendoza</strong> | Gerente General | Ext. 1001</p></div>',
  "red_flags":[],"explanation":"Correo interno legítimo. Dominio corporativo oficial, agenda estructurada, contacto verificable.",
  "legit_reason":"Dominio corporativo · Agenda concreta · Canales de respuesta múltiples · Sin datos sensibles",
  "points":150,"time_limit":25,
},
# ── NIVEL 3: ATAQUES AVANZADOS ────────────────────────────
{
  "id":9,"level":3,"isPhishing":True,
  "from_name":"Roberto Sánchez – CEO","from_email":"r.sanchez@miempresa-corp.net",
  "to":"empleado@miempresa.com","date":"Hoy, 11:02 AM",
  "subject":"CONFIDENCIAL: Transferencia urgente – Adquisición estratégica",
  "body_html":'<div class="em-header" style="background:#b71c1c">CONFIDENCIAL – CEO Office</div><div class="em-body"><p>Hola,</p><p>Estoy en reunión con abogados y <strong>no puedo hablar por teléfono</strong>. Necesito que proceses una transferencia bancaria urgente hoy mismo.</p><p>Estamos cerrando una <strong>adquisición estratégica confidencial</strong>. Por instrucción del consejo, <u>no debe comunicarse internamente hasta su confirmación</u>.</p><div class="em-info-box" style="border-color:#b71c1c;background:#ffebee">Beneficiario: Inversiones Globales LLC | Banco: First National Bank<br>Cuenta: 4782-9901-0023 | Monto: <strong>$47,500 USD</strong></div><p>Procesa y confirma por este mismo correo. <strong>No lo menciones a nadie.</strong></p><p>Roberto Sánchez | CEO, MiEmpresa</p></div>',
  "red_flags":[
    {"icon":"📧","title":"Business Email Compromise (BEC)","desc":"Suplantar al CEO para transferencias es el ataque más costoso según el FBI IC3. +$26 mil millones anuales."},
    {"icon":"🌐","title":"Dominio del CEO diferente al corporativo","desc":"'miempresa-corp.net' vs 'miempresa.com'. Un carácter de diferencia, consecuencias devastadoras."},
    {"icon":"🤫","title":"Solicitud explícita de secreto","desc":"'No lo menciones a nadie' aísla a la víctima e impide que colegas identifiquen el fraude."},
    {"icon":"📵","title":"Bloquea verificación telefónica","desc":"'No puedo hablar por teléfono' elimina el canal de verificación. Ante transferencias, SIEMPRE llama."},
  ],
  "explanation":"Business Email Compromise (BEC). El ataque más costoso del mundo. Verifica transferencias por teléfono directo sin importar quién ordena.",
  "legit_reason":None,"points":200,"time_limit":20,
},
{
  "id":10,"level":3,"isPhishing":False,
  "from_name":"Comunicaciones – MiEmpresa","from_email":"comunicaciones@miempresa.com",
  "to":"empleado@miempresa.com","date":"Hoy, 08:00 AM",
  "subject":"📰 Boletín Interno MiEmpresa | Junio 2024",
  "body_html":'<div class="em-header" style="background:#00695c">📰 Boletín Interno – Junio 2024</div><div class="em-body"><p><strong>🏆 Noticias del mes</strong></p><p><strong>Nuevo cliente:</strong> MiEmpresa firmó contrato con Corporación XYZ por 12 meses.</p><p><strong>Reconocimientos:</strong> El equipo de ventas superó la meta Q2 en un 18%.</p><hr style="border-color:#ddd;margin:12px 0"><p><strong>📅 Próximos eventos:</strong> 20 Jun: Reunión Q2 | 25 Jun: Día de integración | 30 Jun: Cierre contable</p><hr style="border-color:#ddd;margin:12px 0"><p><strong>💡 Tip de seguridad:</strong> El equipo de TI <u>nunca</u> solicitará su contraseña por correo. Reporte a seguridad@miempresa.com.</p><p class="em-footer">Para cancelar suscripción: Intranet → Comunicaciones</p></div>',
  "red_flags":[],"explanation":"Boletín corporativo legítimo. Dominio oficial, sin solicitudes urgentes, desuscripción vía intranet.",
  "legit_reason":"Dominio corporativo · Contenido informativo · Sin acciones urgentes · Desuscripción en intranet",
  "points":200,"time_limit":20,
},
{
  "id":11,"level":3,"isPhishing":True,
  "from_name":"DocuSign","from_email":"firma@docusign-esignature.net",
  "to":"empleado@miempresa.com","date":"Hoy, 10:15 AM",
  "subject":"Documento pendiente: Actualización Contrato Laboral – Vence HOY",
  "body_html":'<div class="em-header" style="background:#FFBE00;color:#333">✍️ DocuSign – Gestión de Documentos</div><div class="em-body"><p>Tiene un documento pendiente de firma de <strong>RRHH – MiEmpresa</strong>:</p><div class="em-info-box" style="border-color:#FFBE00;background:#fffde7">📄 <strong>Documento:</strong> Actualización de términos contractuales 2024<br>📤 <strong>Enviado por:</strong> María González (RRHH)<br>⏰ <strong>Vence:</strong> <span style="color:#cc0000"><strong>Hoy, 5:00 PM</strong></span></div><p><strong>Por favor firme antes de las 5:00 PM para no afectar su próximo pago de nómina.</strong></p><div class="em-cta-wrap"><a class="em-cta" href="#" style="background:#FFBE00;color:#333">✍️ FIRMAR DOCUMENTO AHORA</a></div><p class="em-footer">DocuSign, Inc. | docusign.com</p></div>',
  "red_flags":[
    {"icon":"🌐","title":"Dominio DocuSign falso","desc":"DocuSign opera desde docusign.com. 'docusign-esignature.net' es un dominio impostor."},
    {"icon":"💰","title":"Amenaza directa a la nómina","desc":"Vincular la firma con el pago de salario es manipulación financiera. Los contratos no bloquean nóminas en horas."},
    {"icon":"⏰","title":"Vencimiento el mismo día","desc":"Documentos contractuales con vencimiento de pocas horas son antinatural. Los legales dan 48-72h mínimo."},
    {"icon":"🔍","title":"Verifica con RRHH directamente","desc":"Ante cualquier solicitud de firma laboral, confirma con RRHH por teléfono antes de proceder."},
  ],
  "explanation":"Phishing que abusa de plataformas de firma electrónica. La amenaza a la nómina explota una necesidad básica. Verifica con RRHH antes de firmar.",
  "legit_reason":None,"points":200,"time_limit":20,
},
{
  "id":12,"level":3,"isPhishing":False,
  "from_name":"Gestión de Activos TI","from_email":"licencias@miempresa.com",
  "to":"empleado@miempresa.com","date":"Ayer, 03:00 PM",
  "subject":"Inventario de licencias software – Acción requerida (antes del viernes)",
  "body_html":'<div class="em-header" style="background:#283593">🖥️ TI – Gestión de Activos y Licencias</div><div class="em-body"><p>Estimado equipo,</p><p>Iniciamos el proceso anual de <strong>renovación de licencias 2024–2025</strong>. Necesitamos su colaboración para completar el inventario.</p><div class="em-info-box" style="border-color:#283593;background:#e8eaf6"><strong>Acceso:</strong> Intranet → TI → Inventario de Software 2024<br><strong>Plazo:</strong> Viernes 21 de junio</div><p>El formulario solicita únicamente: nombre del software, versión y frecuencia de uso.</p><p><strong>Nota:</strong> No es necesario proporcionar contraseñas ni claves de licencia.</p><p>Equipo TI | licencias@miempresa.com | Ext. 2250</p></div>',
  "red_flags":[],"explanation":"Correo legítimo de TI. Solo intranet, explica qué se necesita, NO solicita contraseñas, plazo razonable.",
  "legit_reason":"Dominio corporativo · Solo intranet · Sin credenciales requeridas · Transparencia del proceso",
  "points":200,"time_limit":20,
},
# ── NIVEL 4: SPEAR PHISHING ───────────────────────────────
{
  "id":13,"level":4,"isPhishing":True,
  "from_name":"LinkedIn","from_email":"notifications@linkedin-messages.com",
  "to":"empleado@miempresa.com","date":"Hoy, 12:30 PM",
  "subject":"Ana García de TechCorp quiere conectar contigo en LinkedIn",
  "body_html":'<div class="em-header" style="background:#0077b5">💼 LinkedIn</div><div class="em-body"><div class="em-info-box" style="border-color:#0077b5;background:#f3f6f8;display:flex;align-items:center;gap:15px"><div style="width:55px;height:55px;background:#0077b5;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:20px;flex-shrink:0">AG</div><div><strong>Ana García</strong><br>Directora de RRHH | TechCorp<br><span style="color:#0077b5">500+ conexiones en común</span></div></div><p><em>"Hola, vi tu perfil y creo que podríamos colaborar. Tenemos una posición de liderazgo que podría interesarte."</em></p><div class="em-cta-wrap"><a class="em-cta" href="#" style="background:#0077b5">Aceptar invitación</a></div><p class="em-footer">LinkedIn Corporation © 2024</p></div>',
  "red_flags":[
    {"icon":"🌐","title":"Dominio LinkedIn falso","desc":"LinkedIn usa linkedin.com. 'linkedin-messages.com' es dominio impostor."},
    {"icon":"🎣","title":"Phishing de establecimiento de contacto","desc":"Una vez aceptas, el atacante enviará malware o solicitará información confidencial."},
    {"icon":"💼","title":"Oferta laboral como cebo","desc":"El atacante investigó tus aspiraciones profesionales previo al ataque (OSINT). Es spear phishing."},
    {"icon":"📧","title":"Accede directamente a linkedin.com","desc":"Siempre verifica solicitudes accediendo directamente al sitio. Nunca desde emails."},
  ],
  "explanation":"Spear phishing por LinkedIn. Primero establece confianza y luego usa esa conexión para enviar malware o robar información.",
  "legit_reason":None,"points":250,"time_limit":18,
},
{
  "id":14,"level":4,"isPhishing":False,
  "from_name":"Ciberseguridad – MiEmpresa","from_email":"seguridad@miempresa.com",
  "to":"empleado@miempresa.com","date":"Hoy, 09:00 AM",
  "subject":"Actualización de seguridad: Windows Defender KB5034441 – Martes",
  "body_html":'<div class="em-header" style="background:#e65100">🛡️ Equipo de Ciberseguridad – MiEmpresa</div><div class="em-body"><p>Estimado colaborador,</p><p>El <strong>martes 18 de junio</strong>, el sistema WSUS desplegará automáticamente la actualización de seguridad <strong>KB5034441</strong> en todos los equipos.</p><div class="em-info-box" style="border-color:#e65100;background:#fff3e0">✅ <strong>No es necesaria ninguna acción de su parte.</strong><br>La actualización ocurrirá automáticamente durante el reinicio.</div><p>Si experimenta problemas: helpdesk.miempresa.com o Ext. 2200.</p><p>Esta comunicación fue aprobada por el CISO. Verifique en el portal de seguridad (intranet).</p></div>',
  "red_flags":[],"explanation":"Comunicación legítima. Dominio corporativo, sin acción requerida, técnicamente específica (WSUS, KB real), verificable en intranet.",
  "legit_reason":"Dominio corporativo · Sin acción requerida · Técnicamente específico · Verificable en intranet",
  "points":250,"time_limit":18,
},
{
  "id":15,"level":4,"isPhishing":True,
  "from_name":"Servicio de Impuestos Internos","from_email":"notificaciones@sii-tributario.org",
  "to":"empleado@miempresa.com","date":"Hoy, 08:45 AM",
  "subject":"NOTIFICACIÓN OFICIAL: Reembolso de $2,340 pendiente de reclamación",
  "body_html":'<div class="em-header" style="background:#1a237e">🏛️ SERVICIO DE IMPUESTOS INTERNOS – Notificación Oficial</div><div class="em-body"><p>Estimado contribuyente,</p><p>Tras revisar su declaración fiscal, tiene derecho a un <strong>reembolso de $2,340.00</strong> del período fiscal 2023.</p><div class="em-info-box" style="border-color:#1a237e;background:#e8eaf6">Referencia: <strong>REF-2024-TX-88291</strong> | Monto: <strong>$2,340.00 USD</strong><br>Estado: ✅ Aprobado – Pendiente de reclamación | Vencimiento: 30 días</div><p>Para recibir su reembolso, verifique su identidad y proporcione sus <strong>datos bancarios</strong>:</p><div class="em-cta-wrap"><a class="em-cta" href="#" style="background:#1a237e">Reclamar mi Reembolso →</a></div></div>',
  "red_flags":[
    {"icon":"🌐","title":"Dominio gubernamental falso","desc":"Los servicios fiscales usan dominios .gov. 'sii-tributario.org' no es un dominio gubernamental legítimo."},
    {"icon":"💰","title":"Reembolso inesperado como cebo","desc":"La promesa de dinero explota el pensamiento desiderativo. Si no esperabas un reembolso, sospecha."},
    {"icon":"🏦","title":"Datos bancarios por email","desc":"Los organismos fiscales NUNCA piden datos bancarios por email. Los reembolsos usan información ya registrada."},
    {"icon":"⏰","title":"Vencimiento artificial de 30 días","desc":"Urgencia fabricada para actuar antes de consultar con alguien."},
  ],
  "explanation":"Phishing tributario. Combina promesa de dinero con autoridad gubernamental. Objetivo: robar datos bancarios o credenciales fiscales.",
  "legit_reason":None,"points":250,"time_limit":18,
},
{
  "id":16,"level":4,"isPhishing":False,
  "from_name":"Amazon Web Services","from_email":"billing@aws.amazon.com",
  "to":"empleado@miempresa.com","date":"01 Jun 2024, 12:00 AM",
  "subject":"Your AWS bill for May 2024 is ready",
  "body_html":'<div class="em-header" style="background:#232f3e">☁️ Amazon Web Services – Billing</div><div class="em-body"><p>Dear AWS Customer,</p><p>Your AWS invoice for May 2024 is now available.</p><div class="em-info-box" style="background:#f5f5f5;border-color:#232f3e"><strong>Account ID:</strong> 123456789012<br><strong>Billing Period:</strong> May 1 – May 31, 2024<br><strong>Total Charges:</strong> $1,847.23 USD | Payment: Visa ****4521</div><p>To view your invoice, sign in to the <strong>AWS Management Console</strong> at <em>console.aws.amazon.com</em> → Billing.</p><p>Amazon Web Services | billing@aws.amazon.com</p></div>',
  "red_flags":[],"explanation":"Factura legítima de AWS. Dominio oficial aws.amazon.com, datos parciales verificables, acceso directo a consola sin enlace embebido.",
  "legit_reason":"Dominio AWS oficial · Datos parciales verificables · Sin enlace directo embebido · Instrucciones de acceso directo",
  "points":250,"time_limit":18,
},
# ── NIVEL 5: APT / ÉLITE ─────────────────────────────────
{
  "id":17,"level":5,"isPhishing":True,
  "from_name":"GitHub Security","from_email":"noreply@github-security.io",
  "to":"empleado@miempresa.com","date":"Hoy, 09:23 AM",
  "subject":"Critical vulnerability in miempresa/core-api – CVE-2024-3094 (CVSS 10.0)",
  "body_html":'<div class="em-header" style="background:#24292e">🐙 GitHub Security Alert</div><div class="em-body"><p>GitHub detected a <strong>critical vulnerability (CVE-2024-3094)</strong> in <strong>miempresa/core-api</strong>.</p><div class="em-info-box" style="border-color:#ffc107;background:#fff3cd">🔴 <strong>CRITICAL – CVSS Score: 10.0</strong><br>Package: xz-utils (5.6.0 / 5.6.1) | Impact: Remote Code Execution<br>Repository: <strong>miempresa/core-api</strong> (branch: main)</div><p>A malicious actor could exploit this to gain <strong>unauthorized access to your systems</strong>.</p><div class="em-cta-wrap"><a class="em-cta" href="#" style="background:#24292e">View Security Advisory &amp; Patch</a></div><p class="em-footer">GitHub, Inc. | github.com/security</p></div>',
  "red_flags":[
    {"icon":"🌐","title":"Dominio GitHub falso","desc":"GitHub usa github.com. 'github-security.io' es dominio falso para atacar perfiles técnicos."},
    {"icon":"🔬","title":"CVE real usado como cebo","desc":"CVE-2024-3094 es una vulnerabilidad real (backdoor XZ Utils). Los atacantes usan CVEs reales para dar credibilidad."},
    {"icon":"🎯","title":"Nombre de repositorio obtenido por OSINT","desc":"'miempresa/core-api' fue encontrado en GitHub público. Es spear phishing preparado."},
    {"icon":"⚡","title":"CVSS 10.0 genera urgencia técnica extrema","desc":"Los desarrolladores actúan rápido ante críticas. Este sesgo profesional es lo que el atacante explota."},
  ],
  "explanation":"Spear phishing técnico APT. El atacante conoce el repositorio, usa un CVE real y explota el instinto de respuesta inmediata de perfiles técnicos.",
  "legit_reason":None,"points":300,"time_limit":15,
},
{
  "id":18,"level":5,"isPhishing":False,
  "from_name":"Dropbox Business","from_email":"no-reply@dropbox.com",
  "to":"empleado@miempresa.com","date":"Hoy, 11:00 AM",
  "subject":"Laura Martínez shared 'Propuesta Q3 2024.pdf' with you",
  "body_html":'<div class="em-header" style="background:#0061FF">📁 Dropbox Business</div><div class="em-body"><p><strong>Laura Martínez (l.martinez@miempresa.com)</strong> ha compartido un archivo contigo.</p><div class="em-info-box" style="border-color:#0061FF;background:#f0f4ff;display:flex;align-items:center;gap:15px"><span style="font-size:36px">📄</span><div><strong>Propuesta Q3 2024.pdf</strong><br>Compartido por: l.martinez@miempresa.com | Tamaño: 2.4 MB | Modificado: Hoy</div></div><div class="em-cta-wrap"><a class="em-cta" href="#" style="background:#0061FF">Abrir en Dropbox</a></div><p class="em-footer">Recibiste este email porque l.martinez@miempresa.com compartió desde Dropbox Business.</p></div>',
  "red_flags":[],"explanation":"Compartir legítimo de Dropbox. Dominio oficial, remitente del dominio corporativo, nombre de archivo específico y contextualmente relevante.",
  "legit_reason":"Dominio Dropbox oficial · Remitente del dominio corporativo · Nombre de archivo específico · Contexto relevante",
  "points":300,"time_limit":15,
},
{
  "id":19,"level":5,"isPhishing":True,
  "from_name":"Zoom","from_email":"no-reply@zoom-webinar-invite.com",
  "to":"empleado@miempresa.com","date":"Hoy, 08:00 AM",
  "subject":"Capacitación OBLIGATORIA – Cumplimiento y Ética Empresarial – HOY 3 PM",
  "body_html":'<div class="em-header" style="background:#2D8CFF">📹 Zoom Webinar – Convocatoria Oficial</div><div class="em-body"><p>Ha sido convocado a una <strong>capacitación obligatoria</strong> de cumplimiento normativo.</p><div class="em-info-box" style="border-color:#2D8CFF;background:#eff6ff">📋 <strong>Capacitación:</strong> Cumplimiento y Ética Empresarial 2024<br>📅 <strong>Fecha:</strong> <span style="color:#cc0000"><strong>Hoy, 3:00 PM – 5:00 PM</strong></span><br>⚠️ <strong>Asistencia:</strong> OBLIGATORIA – Afecta evaluación de desempeño</div><p>Para unirse, complete el registro. El sistema <strong>solicitará sus credenciales corporativas</strong> para verificar que es empleado autorizado.</p><div class="em-cta-wrap"><a class="em-cta" href="#" style="background:#2D8CFF">Unirse a Zoom – Registro requerido</a></div></div>',
  "red_flags":[
    {"icon":"🌐","title":"Dominio Zoom falso","desc":"Zoom usa zoom.us. 'zoom-webinar-invite.com' es dominio falso."},
    {"icon":"🔑","title":"Zoom no pide credenciales corporativas","desc":"Zoom nunca solicita las credenciales de tu empresa para unirte a una reunión."},
    {"icon":"⚖️","title":"Coerción laboral (evaluación de desempeño)","desc":"Vincular asistencia con evaluación elimina el pensamiento crítico. Táctica avanzada."},
    {"icon":"📅","title":"Capacitación obligatoria comunicada el mismo día","desc":"Una capacitación de compliance comunicada y celebrada el mismo día es operativamente imposible."},
  ],
  "explanation":"Phishing de Zoom que combina autoridad + coerción laboral + urgencia. Las 'credenciales corporativas para verificar identidad' son el robo directo.",
  "legit_reason":None,"points":300,"time_limit":15,
},
{
  "id":20,"level":5,"isPhishing":False,
  "from_name":"Red Team – Ciberseguridad","from_email":"redteam@miempresa.com",
  "to":"empleado@miempresa.com","date":"Hoy, 10:00 AM",
  "subject":"Resultado de su prueba de phishing simulado – Informe personal disponible",
  "body_html":'<div class="em-header" style="background:#1b5e20">✅ Red Team – Ciberseguridad MiEmpresa</div><div class="em-body"><p>Estimado colaborador,</p><p>Como parte del <strong>programa anual de seguridad</strong>, nuestro equipo realizó un <strong>ejercicio controlado de phishing simulado</strong> autorizado por la Dirección General.</p><p>Sus resultados individuales están disponibles en la intranet:</p><div class="em-info-box" style="border-color:#1b5e20;background:#e8f5e9"><strong>Ruta:</strong> Intranet → Seguridad → Resultados Ejercicio Phishing 2024</div><p>Red Team – Ciberseguridad | redteam@miempresa.com | Ext. 2400<br><em>Ejercicio autorizado por: Roberto Sánchez, CEO | María López, CISO</em></p></div>',
  "red_flags":[],"explanation":"Comunicación legítima del Red Team. Dominio corporativo, acceso solo en intranet, cadena de autorización explícita, sin solicitud de datos.",
  "legit_reason":"Dominio corporativo · Solo intranet · Autorización explícita verificable (CEO+CISO) · Sin solicitud de datos",
  "points":300,"time_limit":15,
},
# ── NIVEL 6: AMENAZAS EMERGENTES ─────────────────────────
{
  "id":21,"level":6,"type":"email","isPhishing":True,"categoria":"BEC",
  "from_name":"Dr. Fernando Vásquez — CFO","from_email":"cfo@miempresa-finance.com",
  "to":"empleado@miempresa.com","date":"Hoy, 14:32 PM",
  "subject":"CONFIDENCIAL: Wire transfer para cierre de adquisición — HOY 3pm",
  "body_html":'<div class="em-header" style="background:#1a237e">🏦 Oficina del CFO — Comunicación Confidencial</div><div class="em-body"><p>Hola equipo de pagos,</p><p>Necesito que procesen este wire antes del cierre bancario (3:00 PM). Es para una adquisición estratégica que se cierra hoy. El equipo legal ya está al tanto, pero <strong>por instrucción del abogado externo no puede pasar por los canales normales de aprobación esta vez.</strong></p><div class="em-info-box" style="border-color:#b71c1c;background:#ffebee">Beneficiario: <strong>Meridian Holdings LLC</strong><br>Monto: <strong>$142,800 USD</strong> | Routing: 021000021 | Cta: 7741982301</div><p><strong>No comenten esto con otros colegas hasta que se confirme la operación.</strong> El CEO informará al equipo después de las 5pm.</p><p>— Dr. Fernando Vásquez, CFO</p></div>',
  "red_flags":[
    {"icon":"🌐","title":"Dominio lateral del CFO","desc":"'miempresa-finance.com' vs 'miempresa.com'. El atacante registró un dominio casi idéntico al corporativo."},
    {"icon":"🚫","title":"'No puede pasar por los canales normales'","desc":"Los canales de aprobación existen exactamente para detectar fraudes. Eliminarlos es la táctica central del atacante."},
    {"icon":"🤫","title":"'No comenten' — aislamiento estratégico","desc":"Impide que compañeros identifiquen el fraude. Las adquisiciones reales no requieren silencio del equipo de pagos."},
    {"icon":"⏰","title":"Cierre bancario como presión artificial","desc":"El plazo de las 3:00 PM impide verificación. Regla absoluta: llama al CFO al número que ya conoces."},
  ],
  "explanation":"BEC sofisticado que imita al CFO desde dominio casi idéntico. La instrucción de 'saltarse los canales normales' es la señal definitiva de fraude. Verifica SIEMPRE por teléfono.",
  "legit_reason":None,"points":350,"time_limit":15,
  "meta_q":"¿Por qué 'no puede pasar por los canales normales de aprobación' es la señal más definitiva de fraude BEC?",
  "meta_ops":[
    "Los canales de aprobación existen exactamente para detectar fraudes — eliminarlos intencionalmente revela el engaño",
    "Porque el monto de $142,800 es inusualmente alto para una transferencia corporativa",
    "Porque el plazo de cierre bancario es a las 3:00 PM de hoy mismo",
    "Porque el CFO usa título 'Dr.' que no es habitual en comunicaciones internas"
  ],
  "meta_ok":0,
},
{
  "id":22,"level":6,"type":"email","isPhishing":True,"categoria":"BEC",
  "from_name":"Compensaciones — RRHH","from_email":"compensaciones@rrhh-grupo.net",
  "to":"empleado@miempresa.com","date":"Hoy, 09:15 AM",
  "subject":"Urgente: Actualización de datos bancarios — Ajuste de nómina aprobado",
  "body_html":'<div class="em-header" style="background:#2e7d32">💰 Recursos Humanos — Comité de Compensaciones</div><div class="em-body"><p>Estimada colaboradora,</p><p>El Comité Ejecutivo aprobó un ajuste especial en tu nómina para este mes. Para procesar el depósito adicional, necesitamos que actualices tu información bancaria en el formulario seguro:</p><div class="em-cta-wrap"><a class="em-cta" href="#" style="background:#2e7d32">ACTUALIZAR DATOS BANCARIOS →</a></div><p class="em-footer">https://rrhh-datos-seguros.net/formulario</p><p><strong>IMPORTANTE:</strong> Completa el proceso antes de las 6:00 PM de hoy para que el ajuste se refleje en el pago de este mes.</p></div>',
  "red_flags":[
    {"icon":"🌐","title":"Dominio externo no corporativo","desc":"rrhh-grupo.net y el link rrhh-datos-seguros.net no son el dominio corporativo miempresa.com."},
    {"icon":"🏦","title":"RRHH nunca pide datos bancarios por formulario web externo","desc":"El proceso correcto es en el portal corporativo o presencialmente. Un formulario externo capturará tus datos sin control."},
    {"icon":"💰","title":"'Ajuste especial' — cebo de codicia","desc":"La promesa de dinero extra activa un sesgo emocional que inhibe el pensamiento crítico."},
    {"icon":"⏰","title":"Plazo de hoy para prevenir verificación","desc":"El plazo de 6:00 PM impide verificar con RRHH en persona o por teléfono."},
  ],
  "explanation":"BEC orientado a robo de datos bancarios del empleado. RRHH nunca solicita actualización por formulario externo. El atacante redirigirá futuras nóminas.",
  "legit_reason":None,"points":350,"time_limit":15,
  "meta_q":"¿Por qué RRHH nunca solicita actualización de datos bancarios por formulario web externo?",
  "meta_ops":[
    "El portal corporativo interno es el único canal seguro y auditable — un formulario externo capturará tus datos sin ningún control",
    "Porque los formularios web externos son más lentos que los portales internos",
    "Porque los datos bancarios son demasiado sensibles para cualquier tipo de formulario",
    "Porque RRHH siempre prefiere realizar este proceso en persona sin ninguna excepción"
  ],
  "meta_ok":0,
},
{
  "id":23,"level":6,"type":"qr","isPhishing":True,"categoria":"quishing",
  "from_name":"Control de Acceso — Seguridad","from_email":"acceso@seguridad-corp.net",
  "to":"empleado@miempresa.com","date":"Hoy, 08:00 AM",
  "subject":"OBLIGATORIO: Renovación de badge de acceso — Escanea el QR antes del viernes",
  "body_html":'<div class="em-header" style="background:#212121">🔐 Departamento de Seguridad Física — Control de Acceso</div><div class="em-body"><p>Estimado empleado,</p><p>Nuestro sistema de control de acceso migró a la nueva plataforma de autenticación. <strong>Todos los empleados deben renovar su badge digital antes del viernes.</strong></p><p>Escanea el código QR con tu teléfono para completar el proceso:</p><div class="qr-placeholder" data-url="https://badge-renewal-corp.net/auth"></div><p class="em-footer">URL destino: badge-renewal-corp.net/auth — Empleados que no completen el proceso perderán acceso el lunes.</p></div>',
  "red_flags":[
    {"icon":"📱","title":"QR apunta a dominio externo","desc":"badge-renewal-corp.net no es el dominio corporativo miempresa.com. Los QR ocultan la URL — el atacante lo sabe."},
    {"icon":"🏢","title":"Badge renewal nunca se hace por QR en email","desc":"Las renovaciones de badge se hacen presencialmente en Recepción o Seguridad, nunca por link externo."},
    {"icon":"🌐","title":"Remitente en dominio no corporativo","desc":"seguridad-corp.net no es el dominio real de la empresa. Seguridad interna usa @miempresa.com."},
    {"icon":"😨","title":"Amenaza de perder acceso físico","desc":"Perder acceso a instalaciones crea pánico inmediato. Táctica de presión para saltarse la verificación."},
  ],
  "explanation":"Quishing (QR phishing): los QR son peligrosos porque la URL destino no es visible antes de escanear. Siempre verifica el remitente y confirma con Seguridad antes de escanear.",
  "legit_reason":None,"points":350,"time_limit":15,
  "meta_q":"¿Por qué los códigos QR son especialmente efectivos como vector de phishing?",
  "meta_ops":[
    "La URL destino no es visible antes de escanear — el usuario no puede verificarla como lo haría con un enlace de texto",
    "Porque los QR son difíciles de distinguir entre sí visualmente en un email",
    "Porque los teléfonos móviles tienen menos protecciones de seguridad que las computadoras",
    "Porque los QR corporativos siempre parecen más oficiales y confiables que los enlaces"
  ],
  "meta_ok":0,
},
{
  "id":24,"level":6,"type":"sms","isPhishing":True,"categoria":"smishing",
  "from_name":"Número desconocido","from_email":"+1 (855) 247-9031",
  "to":"Tu teléfono","date":"Hoy, 10:14 AM",
  "subject":"SMS de Alerta TI",
  "body_html":"ALERTA IT CORP: Tu cuenta O365 fue comprometida. Verifica AHORA: http://it-secure-verify.net/o365 — perderás acceso en 2h. No respondas. Ref: INC-20249",
  "red_flags":[
    {"icon":"📱","title":"Número de teléfono externo desconocido","desc":"El helpdesk interno tiene un número registrado. Un número +1 (855) externo nunca envía alertas corporativas reales."},
    {"icon":"🌐","title":"URL en dominio externo","desc":"it-secure-verify.net no es el dominio corporativo. TI real usa portales internos conocidos para reseteos."},
    {"icon":"⏰","title":"2 horas: urgencia extrema por SMS","desc":"Los ataques por SMS explotan la inmediatez del canal. TI real usa el sistema de tickets con tiempo razonable."},
    {"icon":"✍️","title":"Sin tildes y errores gramaticales","desc":"'perderás' vs errores de puntuación son señales de mensaje automatizado malicioso."},
  ],
  "explanation":"Smishing (SMS phishing). TI real nunca usa números externos para alertas corporativas. El link captura credenciales de O365 — correo, Teams, OneDrive.",
  "legit_reason":None,"points":350,"time_limit":15,
  "meta_q":"¿Cuál es la señal más definitiva de que este SMS de alerta O365 es smishing y no una alerta real del equipo de TI?",
  "meta_ops":[
    "El número es externo (+1 855) y la URL apunta a un dominio ajeno al corporativo — TI real usa canales conocidos",
    "Porque el SMS no tiene el logo ni los colores de la empresa en el mensaje",
    "Porque los SMS de alertas de TI siempre deben incluir el nombre del técnico responsable",
    "Porque el link usa HTTP en lugar de HTTPS lo que lo hace inseguro automáticamente"
  ],
  "meta_ok":0,
},
{
  "id":25,"level":6,"type":"qr","isPhishing":False,
  "from_name":"Laura Ríos — Coordinadora de Eventos","from_email":"eventos@miempresa.com",
  "to":"empleado@miempresa.com","date":"Hoy, 11:00 AM",
  "subject":"Código QR de acceso — Evento corporativo jueves 15 de mayo",
  "body_html":'<div class="em-header" style="background:#00695c">🎉 Coordinación de Eventos — MiEmpresa</div><div class="em-body"><p>Hola equipo,</p><p>Adjunto el código QR de acceso para el evento corporativo del próximo jueves. Escanea para confirmar tu asistencia y obtener acceso al salón:</p><div class="qr-placeholder" data-url="https://eventos.miempresa.com/confirm/EVT-2025-05"></div><p class="em-footer">URL destino: eventos.miempresa.com/confirm/EVT-2025-05</p><p>Cualquier duda, contáctame directamente.<br><strong>Laura Ríos</strong> — Coordinadora de Eventos | eventos@miempresa.com | Ext. 3201</p></div>',
  "red_flags":[],"explanation":"QR corporativo legítimo. El remitente es del dominio corporativo real (@miempresa.com) y la URL del QR apunta al subdominio corporativo conocido (eventos.miempresa.com).",
  "legit_reason":"Remitente @miempresa.com · URL del QR en subdominio corporativo · Persona verificable con extensión · Sin urgencia ni amenazas",
  "points":350,"time_limit":15,
},
{
  "id":26,"level":6,"type":"sms","isPhishing":False,
  "from_name":"Marriott Rewards","from_email":"+506 2234-5678",
  "to":"Tu teléfono","date":"Hoy, 09:03 AM",
  "subject":"SMS de confirmación de reserva",
  "body_html":"Reserva confirmada. Hotel Marriott Reforma, check-in 18 mayo. Código: MXC-4491. Para asistencia llama al +52 55 9138-4888. Marriott Rewards.",
  "red_flags":[],"explanation":"SMS legítimo de confirmación de reserva. No contiene ningún enlace, no solicita acción, incluye información verificable y número de contacto opcional.",
  "legit_reason":"Sin enlace ni URL · Solo información verificable · Número de contacto opcional · Sin urgencia ni solicitud de datos",
  "points":350,"time_limit":15,
},
]

LEVELS = {
    "1":{"name":"Amenazas Básicas",    "color":"#00ff88"},
    "2":{"name":"Nivel Intermedio",    "color":"#4a9eff"},
    "3":{"name":"Ataques Avanzados",   "color":"#ff9f0a"},
    "4":{"name":"Spear Phishing",      "color":"#bf5af2"},
    "5":{"name":"APT / Élite",         "color":"#ff2d55"},
    "6":{"name":"Amenazas Emergentes", "color":"#00e5ff"},
}

BADGES = [
    {"id":"first",  "ic":"🎮","nm":"Primera Misión",   "ds":"Completar el primer correo"},
    {"id":"lvl1",   "ic":"🎣","nm":"Cazador de Phish", "ds":"Superar el Nivel 1"},
    {"id":"lvl3",   "ic":"🔍","nm":"Detective Digital", "ds":"Superar el Nivel 3"},
    {"id":"lvl5",   "ic":"🏆","nm":"Agente PhishGuard", "ds":"Completar los 6 niveles"},
    {"id":"combo5", "ic":"🦅","nm":"Ojo de Águila",     "ds":"5 aciertos consecutivos"},
    {"id":"speed",  "ic":"⚡","nm":"Velocidad Máxima",  "ds":"Responder en menos de 5 segundos"},
    {"id":"shield", "ic":"🛡️","nm":"Escudo de Acero",  "ds":"Nivel completo sin perder vidas"},
    {"id":"elite",  "ic":"💎","nm":"Gran Maestro",       "ds":"Puntuación final mayor a 5,000 pts"},
]

RANKS = [
    {"min":0,    "label":"Aprendiz",        "color":"#5a7aaa","bg":"rgba(90,122,170,.15)"},
    {"min":1000, "label":"Analista",        "color":"#00e5ff","bg":"rgba(0,229,255,.12)"},
    {"min":3000, "label":"Investigador",    "color":"#00ff88","bg":"rgba(0,255,136,.12)"},
    {"min":6000, "label":"Especialista",    "color":"#ff9f0a","bg":"rgba(255,159,10,.12)"},
    {"min":10000,"label":"Experto",         "color":"#bf5af2","bg":"rgba(191,90,242,.12)"},
    {"min":14000,"label":"Agente de Élite", "color":"#ffd60a","bg":"rgba(255,214,10,.15)"},
]

MISSIONS_POOL = [
    {"id":1,"emoji":"🎯","titulo":"Sin errores Nivel 1","desc":"Completa el Nivel 1 sin cometer ningún error","tipo":"nivel_perfecto","nivel":1,"meta":1,"xp":100},
    {"id":2,"emoji":"🔥","titulo":"Racha de fuego","desc":"Consigue 5 respuestas correctas consecutivas","tipo":"racha","meta":5,"xp":150},
    {"id":3,"emoji":"⚡","titulo":"Velocista","desc":"Responde 3 correos en menos de 8 segundos","tipo":"velocidad","meta":3,"xp":120},
    {"id":4,"emoji":"🕵️","titulo":"Detector BEC","desc":"Identifica correctamente 2 ataques BEC","tipo":"categoria","cat":"BEC","meta":2,"xp":200},
    {"id":5,"emoji":"🧠","titulo":"Mente analítica","desc":"Acierta 3 preguntas de metacognición seguidas","tipo":"meta_racha","meta":3,"xp":180},
    {"id":6,"emoji":"❤️","titulo":"Intocable","desc":"Completa cualquier nivel sin perder ninguna vida","tipo":"nivel_sin_vida","meta":1,"xp":160},
    {"id":7,"emoji":"📱","titulo":"Maestro QR","desc":"Detecta correctamente los 2 ataques de quishing","tipo":"categoria","cat":"quishing","meta":2,"xp":220},
    {"id":8,"emoji":"🏆","titulo":"Puntaje élite","desc":"Acumula más de 8,000 puntos en una partida","tipo":"puntaje","meta":8000,"xp":250},
    {"id":9,"emoji":"💬","titulo":"SMS sin trampa","desc":"Detecta los 2 ataques smishing correctamente","tipo":"categoria","cat":"smishing","meta":2,"xp":200},
]

# ══════════════════════════════════════════════════════════
#  CSS, HTML Y MOTOR DE JUEGO
# ══════════════════════════════════════════════════════════
CSS = '''
:root{--bg0:#05080f;--bg1:#0b1222;--bg2:#111a30;--bg3:#18243e;
  --cyan:#00e5ff;--green:#00ff88;--red:#ff2d55;--orange:#ff9f0a;
  --yellow:#ffd60a;--purple:#bf5af2;--blue:#4a9eff;
  --text:#dce8ff;--dim:#4e6b99;--border:rgba(0,229,255,.13);
  --mono:'Courier New',monospace;--ui:'Segoe UI',system-ui,sans-serif;
  --r8:8px;--r12:12px;--r16:16px;--r24:24px;--r32:32px;}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;overflow-x:hidden}
body{font-family:var(--ui);background:var(--bg0);color:var(--text);min-height:100vh}
a{pointer-events:none;text-decoration:none;color:inherit}
button{font-family:var(--ui);cursor:pointer}
canvas#stars-bg{position:fixed;inset:0;z-index:0;pointer-events:none}
.scr{display:none;flex-direction:column;align-items:center;justify-content:center;
     min-height:100vh;position:relative;z-index:1;padding:20px 16px}
.scr.on{display:flex}
body::after{content:'';position:fixed;inset:0;z-index:0;pointer-events:none;
  background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,0,0,.04) 2px,rgba(0,0,0,.04) 4px);}
.t-glow-c{color:var(--cyan);text-shadow:0 0 20px rgba(0,229,255,.5)}
.t-glow-g{color:var(--green);text-shadow:0 0 20px rgba(0,255,136,.4)}
.t-glow-r{color:var(--red);text-shadow:0 0 20px rgba(255,45,85,.5)}
.t-glow-y{color:var(--yellow);text-shadow:0 0 20px rgba(255,214,10,.5)}
.t-mono{font-family:var(--mono)}.t-dim{color:var(--dim)}.t-upper{text-transform:uppercase;letter-spacing:3px}
.card{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r12);padding:16px 20px}
.btn{border:none;border-radius:var(--r32);font-weight:800;letter-spacing:2px;
     text-transform:uppercase;transition:.18s;cursor:pointer;display:inline-flex;
     align-items:center;justify-content:center;gap:8px}
.btn:active{transform:scale(.97)}
.btn-cyan{background:linear-gradient(135deg,var(--cyan),#0099cc);color:#000;box-shadow:0 0 28px rgba(0,229,255,.35)}
.btn-cyan:hover{box-shadow:0 0 50px rgba(0,229,255,.6);transform:scale(1.04)}
.btn-outline{background:transparent;color:var(--cyan);border:2px solid var(--cyan)}
.btn-outline:hover{background:rgba(0,229,255,.08)}
.btn-success{background:linear-gradient(135deg,#00ff88,#00a854);color:#000;box-shadow:0 0 20px rgba(0,255,136,.25)}
.btn-lg{font-size:16px;padding:15px 44px}.btn-md{font-size:14px;padding:12px 32px}.btn-sm{font-size:12px;padding:9px 22px}
#hud{position:fixed;top:0;left:0;right:0;z-index:200;background:rgba(5,8,15,.94);
     border-bottom:1px solid var(--border);backdrop-filter:blur(14px);padding:8px 16px;
     display:none;align-items:center;gap:10px;flex-wrap:wrap;min-height:58px}
.hb{display:flex;flex-direction:column;align-items:center;min-width:52px}
.hl{font-size:8px;color:var(--dim);text-transform:uppercase;letter-spacing:2px;font-family:var(--mono);white-space:nowrap}
.hv{font-size:18px;font-weight:800;font-family:var(--mono);line-height:1.1}
.hsep{width:1px;height:38px;background:var(--border);flex-shrink:0}.hsp{flex:1}
#hv-score .hv{color:var(--cyan)}#hv-combo .hv{color:var(--yellow);transition:color .3s}
#hv-lives .hv{font-size:15px}#hv-timer .hv{color:var(--orange);font-size:22px}#hv-level .hv{color:var(--green)}
.hprog{flex:1;min-width:100px}
.hprog-bar{height:5px;background:var(--bg3);border-radius:4px;overflow:hidden;margin-top:5px}
.hprog-fill{height:100%;background:linear-gradient(90deg,var(--cyan),var(--green));border-radius:4px;transition:width .45s ease}
#hud-badges{display:flex;gap:4px;align-items:center;margin-left:6px}
.bdg-mini{font-size:18px;animation:pop .35s}
#toasts{position:fixed;top:66px;right:14px;z-index:500;
        display:flex;flex-direction:column;gap:7px;pointer-events:none;max-width:280px}
.toast{border-radius:var(--r8);padding:9px 14px;font-size:12px;font-weight:700;animation:toastIn .3s ease;border:1px solid}
.tc{border-color:var(--cyan);color:var(--cyan);background:rgba(0,229,255,.1)}
.tg{border-color:var(--green);color:var(--green);background:rgba(0,255,136,.08)}
.tr{border-color:var(--red);color:var(--red);background:rgba(255,45,85,.1)}
.ty{border-color:var(--yellow);color:var(--yellow);background:rgba(255,214,10,.08)}
#s-intro{gap:18px;text-align:center}
.logo-anim{font-size:88px;animation:float 3s ease-in-out infinite;filter:drop-shadow(0 0 30px rgba(0,229,255,.5))}
.game-title{font-size:clamp(38px,7vw,78px);font-weight:900;letter-spacing:5px;
            background:linear-gradient(135deg,var(--cyan) 0%,var(--green) 100%);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
            filter:drop-shadow(0 0 24px rgba(0,229,255,.4))}
.game-sub{font-size:clamp(11px,2vw,16px);color:var(--dim);letter-spacing:7px;font-family:var(--mono)}
.game-desc{max-width:500px;font-size:14px;color:#7c9bbf;line-height:1.75}
.intro-stats{display:flex;gap:12px;flex-wrap:wrap;justify-content:center}
.istat{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r12);padding:12px 18px;text-align:center}
.istat-v{font-size:28px;font-weight:900;color:var(--cyan)}
.istat-l{font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:2px;margin-top:2px}
.kb-hint{font-size:11px;color:var(--dim);font-family:var(--mono);margin-top:4px}
.intro-missions-wrap{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r12);
  padding:14px 18px;max-width:460px;width:100%}
.intro-missions-hdr{display:flex;align-items:center;justify-content:space-between;
  font-size:11px;color:var(--cyan);text-transform:uppercase;letter-spacing:2px;font-family:var(--mono);margin-bottom:10px}
.intro-mission-row{display:flex;align-items:center;gap:10px;padding:6px 0;border-bottom:1px solid var(--border)}
.intro-mission-row:last-child{border:none}.intro-mission-row.done{opacity:.6}
#intro-xp-avail{font-size:11px;color:var(--yellow);margin-top:8px;text-align:center;font-weight:700}
#s-misiones{gap:14px;text-align:center}
.ms-icon{font-size:60px;animation:float 3s ease-in-out infinite}
.ms-title{font-size:34px;font-weight:900;letter-spacing:3px}.ms-fecha{font-size:11px;letter-spacing:2px}
#ms-xp-total{font-size:12px;color:var(--yellow);font-weight:700}
.mission-card{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r12);
  padding:14px 18px;max-width:520px;width:100%;display:flex;align-items:center;gap:14px;text-align:left}
.mission-card.done{border-color:rgba(0,255,136,.3);background:rgba(0,255,136,.04)}
.mission-emoji{font-size:26px;flex-shrink:0}.mission-info{flex:1}
.mission-name{font-size:14px;font-weight:700;margin-bottom:3px}
.mission-desc{font-size:12px;color:var(--dim);line-height:1.4}
.mission-prog-wrap{display:flex;align-items:center;gap:8px;margin-top:7px}
.mission-prog-bar{flex:1;height:4px;background:var(--bg3);border-radius:4px;overflow:hidden}
.mission-prog-fill{height:100%;background:var(--cyan);border-radius:4px;transition:width .4s}
.mission-prog-text{font-size:10px;color:var(--dim);font-family:var(--mono)}
.mission-xp{font-size:13px;color:var(--yellow);font-weight:800;flex-shrink:0}
#s-game{padding-top:72px;padding-bottom:80px;justify-content:flex-start;
        align-items:stretch;max-width:860px;margin:0 auto;width:100%}
.lvl-banner{text-align:center;padding:10px 16px;margin-bottom:14px;background:var(--bg2);
            border:1px solid var(--border);border-radius:var(--r8);font-family:var(--mono);font-size:12px;color:var(--dim)}
.lvl-banner span{color:var(--cyan);font-weight:700}
.email-card{background:var(--bg1);border:1px solid var(--border);border-radius:var(--r16);
            overflow:hidden;box-shadow:0 10px 50px rgba(0,0,0,.6)}
.email-tb{background:var(--bg2);padding:11px 14px;display:flex;align-items:center;gap:9px;border-bottom:1px solid var(--border)}
.dot{width:11px;height:11px;border-radius:50%}
.tb-lbl{font-size:11px;color:var(--dim);font-family:var(--mono);margin-left:6px}
.email-meta{padding:14px 18px;border-bottom:1px solid var(--border);background:var(--bg2)}
.ef{display:flex;gap:8px;margin-bottom:5px;font-size:12px}
.ef-k{color:var(--dim);min-width:48px;font-family:var(--mono)}.ef-v{color:var(--text)}
.email-subj{padding:12px 18px;border-bottom:1px solid var(--border);font-size:15px;font-weight:700;color:var(--text);background:var(--bg1)}
.email-body{background:#fff;color:#222;min-height:200px;padding:18px 20px;font-size:13px;line-height:1.65}
.email-body .em-header{color:#fff;padding:13px 16px;border-radius:8px 8px 0 0;font-size:15px;font-weight:700}
.email-body .em-body{padding:14px;border:1px solid #ddd;border-top:none;border-radius:0 0 8px 8px}
.email-body .em-body p{margin-bottom:9px}
.email-body .em-body ul,.email-body .em-body ol{margin:6px 0 6px 18px}
.email-body .em-cta-wrap{text-align:center;margin:16px 0}
.email-body .em-cta{display:inline-block;padding:10px 24px;border-radius:6px;font-weight:700;font-size:13px;color:#fff;cursor:default}
.email-body .em-info-box{border:1px solid #ccc;border-radius:6px;padding:11px 13px;margin:10px 0;font-size:12px;line-height:1.6}
.email-body .em-footer{font-size:11px;color:#999;margin-top:8px}
.email-body hr{border:none;border-top:1px solid #ddd}
.qr-placeholder{display:flex;justify-content:center;padding:12px 0}
.sms-frame{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r16);
           overflow:hidden;max-width:420px;margin:0 auto;box-shadow:0 10px 50px rgba(0,0,0,.6)}
.sms-topbar{background:var(--bg3);padding:12px 16px;display:flex;align-items:center;
            gap:10px;border-bottom:1px solid var(--border)}
.sms-contact-ico{width:38px;height:38px;background:var(--cyan);color:#000;border-radius:50%;
  display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:900;flex-shrink:0}
.sms-contact-info{flex:1}
.sms-contact-name{font-size:14px;font-weight:700}.sms-contact-num{font-size:11px;color:var(--dim);font-family:var(--mono)}
.sms-body{background:#e5ddd5;padding:16px;min-height:180px}
.sms-date-sep{text-align:center;font-size:11px;color:#555;margin-bottom:12px;
  background:rgba(255,255,255,.6);border-radius:12px;padding:3px 10px}
.sms-bubble-wrap{display:flex;flex-direction:column;align-items:flex-start}
.sms-bubble{background:#fff;border-radius:0 12px 12px 12px;padding:10px 14px;
  font-size:13px;line-height:1.65;color:#222;max-width:88%;word-break:break-word}
.sms-time{font-size:10px;color:#888;margin-top:4px;margin-left:6px}
.sms-hint{text-align:center;font-size:11px;color:var(--dim);padding:8px;
  border-top:1px solid var(--border);font-family:var(--mono);background:var(--bg2)}
#action-bar{position:fixed;bottom:0;left:0;right:0;z-index:200;background:rgba(5,8,15,.94);
            border-top:1px solid var(--border);backdrop-filter:blur(14px);padding:10px 16px;
            display:none;gap:12px;justify-content:center;align-items:center}
.btn-classify{flex:1;max-width:350px;padding:13px 18px;border-radius:var(--r12);border:none;
              cursor:pointer;font-size:14px;font-weight:800;letter-spacing:1px;
              text-transform:uppercase;transition:.15s;display:flex;align-items:center;
              justify-content:center;gap:8px;font-family:var(--ui)}
.btn-classify:disabled{opacity:.5;cursor:not-allowed;transform:none!important}
.btn-phish{background:linear-gradient(135deg,#ff2d55,#b0002a);color:#fff;box-shadow:0 4px 20px rgba(255,45,85,.4)}
.btn-phish:hover:not(:disabled){transform:scale(1.03);box-shadow:0 6px 32px rgba(255,45,85,.7)}
.btn-legit{background:linear-gradient(135deg,#00ff88,#009050);color:#000;box-shadow:0 4px 20px rgba(0,255,136,.3)}
.btn-legit:hover:not(:disabled){transform:scale(1.03);box-shadow:0 6px 32px rgba(0,255,136,.6)}
.kh{font-size:9px;opacity:.55;font-family:var(--mono);display:block;font-weight:400}
#meta-overlay{position:fixed;inset:0;z-index:350;background:rgba(0,0,0,.88);
  backdrop-filter:blur(12px);display:none;align-items:center;justify-content:center;padding:16px}
#meta-overlay.on{display:flex}
.meta-box{background:var(--bg1);border:1px solid rgba(191,90,242,.5);border-radius:var(--r24);
  max-width:580px;width:100%;padding:24px;box-shadow:0 0 60px rgba(191,90,242,.15);animation:slideUp .25s ease}
.meta-badge{font-size:10px;color:var(--purple);text-transform:uppercase;letter-spacing:3px;
  font-family:var(--mono);margin-bottom:5px}
.meta-subtitle{font-size:12px;color:var(--dim);margin-bottom:14px;line-height:1.5}
.meta-q{font-size:15px;font-weight:700;margin-bottom:16px;line-height:1.5;color:var(--text)}
.meta-option{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r8);
  padding:11px 14px;font-size:13px;cursor:pointer;margin-bottom:8px;transition:.15s;
  display:flex;align-items:flex-start;gap:10px;text-align:left;width:100%;
  color:var(--text);font-family:var(--ui);line-height:1.5}
.meta-option:hover:not(:disabled){border-color:var(--purple);background:rgba(191,90,242,.08)}
.meta-option.correct{border-color:var(--green)!important;background:rgba(0,255,136,.1)!important;color:var(--green)!important}
.meta-option.wrong{border-color:var(--red)!important;background:rgba(255,45,85,.08)!important;color:var(--red)!important}
.meta-option:disabled{cursor:not-allowed}
.mopt-key{min-width:22px;height:22px;border:1px solid var(--dim);border-radius:4px;
  display:flex;align-items:center;justify-content:center;font-size:11px;
  font-family:var(--mono);flex-shrink:0;margin-top:1px;font-weight:700}
.mopt-text{flex:1}
.meta-xp{text-align:center;font-size:13px;font-weight:700;min-height:22px;margin-top:8px;color:var(--purple)}
#modal{position:fixed;inset:0;z-index:300;background:rgba(0,0,0,.8);
       backdrop-filter:blur(8px);display:none;align-items:center;justify-content:center;padding:16px}
#modal.on{display:flex}
.modal-box{background:var(--bg1);border-radius:var(--r24);max-width:680px;width:100%;
           max-height:88vh;overflow-y:auto;border:1px solid var(--border);
           box-shadow:0 24px 80px rgba(0,0,0,.85);animation:slideUp .28s ease}
.modal-hdr{padding:18px 22px;display:flex;align-items:center;gap:14px;border-bottom:1px solid var(--border)}
.modal-ico{font-size:46px;flex-shrink:0}.modal-verd{font-size:20px;font-weight:900}
.modal-pts{font-size:12px;color:var(--dim);font-family:var(--mono);margin-top:3px}
.modal-body-inner{padding:18px 22px}
.modal-expl{font-size:13px;line-height:1.75;color:#9bbcde;background:var(--bg2);
            padding:13px 16px;border-radius:var(--r8);margin-bottom:14px;border-left:3px solid var(--cyan)}
.flags-hdr{font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:2px;
           font-family:var(--mono);margin-bottom:8px}
.flag{display:flex;gap:11px;align-items:flex-start;padding:9px 12px;
      background:var(--bg2);border:1px solid var(--border);border-radius:var(--r8);margin-bottom:7px}
.flag-ic{font-size:20px;flex-shrink:0;margin-top:1px}
.flag-ti{font-size:12px;font-weight:700;color:var(--orange);margin-bottom:2px}
.flag-ds{font-size:11px;color:var(--dim);line-height:1.5}
.legit-box{background:rgba(0,255,136,.07);border:1px solid rgba(0,255,136,.2);
           border-radius:var(--r8);padding:11px 14px;font-size:12px;color:#6effc0;margin-bottom:12px}
.modal-ft{padding:14px 22px;border-top:1px solid var(--border);display:flex;justify-content:center}
#s-level{gap:18px;text-align:center}
.lc-icon{font-size:72px;animation:float 2s ease-in-out infinite}.lc-title{font-size:46px;font-weight:900}
.lc-sub{font-size:12px;color:var(--dim);font-family:var(--mono);letter-spacing:4px}
.lc-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:12px;max-width:480px;width:100%}
.lcs{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r12);padding:14px;text-align:center}
.lcs-v{font-size:30px;font-weight:900;color:var(--cyan)}
.lcs-l{font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:1px;margin-top:2px}
.badge-earned{background:var(--bg2);border:2px solid var(--yellow);border-radius:var(--r16);
             padding:14px 22px;max-width:320px;text-align:center;animation:pop .5s}
.be-ic{font-size:46px}.be-nm{font-size:14px;font-weight:700;color:var(--yellow);margin-top:6px}
.be-ds{font-size:11px;color:var(--dim);margin-top:3px}
#s-gameover{gap:18px;text-align:center}
.go-icon{font-size:88px;animation:shake .5s ease}.go-title{font-size:54px;font-weight:900}
.go-msg{font-size:14px;color:var(--dim);max-width:420px;line-height:1.75}
.go-score-wrap{text-align:center}
.go-score-lbl{font-size:11px;color:var(--dim);text-transform:uppercase;letter-spacing:3px;margin-bottom:4px}
.go-score{font-size:52px;font-weight:900;font-family:var(--mono)}
.go-summary{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r12);
            padding:14px 20px;max-width:400px;width:100%;text-align:left}
.go-sum-row{display:flex;justify-content:space-between;font-size:13px;padding:6px 0;border-bottom:1px solid var(--border)}
.go-sum-row:last-child{border:none}.go-sum-row .k{color:var(--dim)}.go-sum-row .v{font-weight:700;font-family:var(--mono)}
#s-victory{gap:18px;text-align:center}
.vc-icon{font-size:88px;animation:float 2s ease-in-out infinite}
.vc-title{font-size:clamp(28px,5vw,58px);font-weight:900;letter-spacing:2px;
          background:linear-gradient(135deg,var(--yellow),var(--orange));
          -webkit-background-clip:text;-webkit-text-fill-color:transparent;
          filter:drop-shadow(0 0 22px rgba(255,214,10,.5))}
.vc-score{font-size:56px;font-weight:900;font-family:var(--mono);color:var(--cyan)}
.results-table{max-width:640px;width:100%;background:var(--bg2);border:1px solid var(--border);border-radius:var(--r12);overflow:hidden}
.rt-head{display:grid;grid-template-columns:80px 1fr 70px 70px 70px 80px;gap:0;background:var(--bg3);padding:10px 16px;
         font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:1px;font-family:var(--mono)}
.rt-row{display:grid;grid-template-columns:80px 1fr 70px 70px 70px 80px;gap:0;padding:10px 16px;
        border-top:1px solid var(--border);font-size:13px;align-items:center}
.rt-row:hover{background:var(--bg3)}
.rt-total{display:grid;grid-template-columns:80px 1fr 70px 70px 70px 80px;gap:0;padding:10px 16px;
          border-top:2px solid var(--cyan);font-weight:800;font-size:13px;background:var(--bg3)}
.badges-gallery{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;max-width:520px}
.bg-card{background:var(--bg2);border:1px solid rgba(255,214,10,.25);border-radius:var(--r8);
         padding:8px 14px;font-size:12px;display:flex;align-items:center;gap:7px}
.bg-card .bi{font-size:22px}
.tips-box{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r12);
          padding:16px 20px;max-width:580px;width:100%;text-align:left}
.tips-title{font-size:11px;color:var(--cyan);text-transform:uppercase;letter-spacing:2px;margin-bottom:12px;font-family:var(--mono)}
.tip{display:flex;gap:10px;font-size:12px;color:var(--dim);margin-bottom:8px;line-height:1.55}
.tip .tn{color:var(--green);flex-shrink:0;font-family:var(--mono);font-weight:700}
.rank-badge{padding:10px 28px;border-radius:var(--r32);font-size:14px;font-weight:800;
            letter-spacing:2px;text-transform:uppercase;margin-top:4px;display:inline-block}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
@keyframes pop{0%{transform:scale(.4);opacity:0}70%{transform:scale(1.12)}100%{transform:scale(1);opacity:1}}
@keyframes slideUp{from{transform:translateY(28px);opacity:0}to{transform:translateY(0);opacity:1}}
@keyframes shake{0%,100%{transform:translateX(0)}20%{transform:translateX(-9px)}40%{transform:translateX(9px)}60%{transform:translateX(-5px)}80%{transform:translateX(5px)}}
@keyframes toastIn{from{transform:translateX(60px);opacity:0}to{transform:translateX(0);opacity:1}}
@keyframes timerPulse{0%,100%{opacity:1}50%{opacity:.3}}
@keyframes comboPop{0%{transform:scale(1.5)}100%{transform:scale(1)}}
@keyframes hudFlash{0%,100%{box-shadow:none}50%{box-shadow:0 0 24px rgba(255,45,85,.7)}}
.timer-warn{animation:timerPulse .55s ease-in-out infinite}
.combo-anim{animation:comboPop .3s ease}
::-webkit-scrollbar{width:6px}::-webkit-scrollbar-track{background:var(--bg1)}
::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:4px}
'''

HTML_BODY = '''
<canvas id="stars-bg"></canvas>
<div id="toasts"></div>

<!-- ══ META-OVERLAY ══ -->
<div id="meta-overlay">
  <div class="meta-box">
    <div class="meta-badge">🧠 METACOGNICIÓN — Antes de ver la explicación</div>
    <div class="meta-subtitle">¿Cuál era la señal clave que deberías haber identificado primero?</div>
    <div class="meta-q" id="meta-q"></div>
    <button class="meta-option" id="meta-opt-0" onclick="G.evalMeta(0)">
      <span class="mopt-key">A</span><span class="mopt-text" id="mopt-text-0"></span>
    </button>
    <button class="meta-option" id="meta-opt-1" onclick="G.evalMeta(1)">
      <span class="mopt-key">B</span><span class="mopt-text" id="mopt-text-1"></span>
    </button>
    <button class="meta-option" id="meta-opt-2" onclick="G.evalMeta(2)">
      <span class="mopt-key">C</span><span class="mopt-text" id="mopt-text-2"></span>
    </button>
    <button class="meta-option" id="meta-opt-3" onclick="G.evalMeta(3)">
      <span class="mopt-key">D</span><span class="mopt-text" id="mopt-text-3"></span>
    </button>
    <div class="meta-xp" id="meta-xp-msg"></div>
  </div>
</div>

<!-- ══ HUD ══ -->
<div id="hud">
  <div class="hb" id="hv-level"><div class="hl">Nivel</div><div class="hv" id="hval-level" style="color:var(--green)">1</div></div>
  <div class="hsep"></div>
  <div class="hb" id="hv-score"><div class="hl">Puntos</div><div class="hv" id="hval-score">0</div></div>
  <div class="hsep"></div>
  <div class="hb" id="hv-combo"><div class="hl">Combo</div><div class="hv" id="hval-combo">x1</div></div>
  <div class="hsep"></div>
  <div class="hb"><div class="hl">Vidas</div><div class="hv" id="hval-lives">❤️❤️❤️</div></div>
  <div class="hsep"></div>
  <div class="hb" id="hv-timer"><div class="hl">Tiempo</div><div class="hv" id="hval-timer">30</div></div>
  <div class="hsp"></div>
  <div class="hprog">
    <div class="hl">Progreso nivel</div>
    <div class="hprog-bar"><div class="hprog-fill" id="hval-prog" style="width:0%"></div></div>
  </div>
  <div id="hud-badges"></div>
</div>

<!-- ══ ACTION BAR ══ -->
<div id="action-bar">
  <button class="btn-classify btn-phish" id="btn-phish" onclick="G.pick(true)">
    🎣 ES PHISHING <span class="kh">tecla F</span>
  </button>
  <button class="btn-classify btn-legit" id="btn-legit" onclick="G.pick(false)">
    ✅ ES LEGÍTIMO <span class="kh">tecla L</span>
  </button>
</div>

<!-- ══ INTRO ══ -->
<div class="scr on" id="s-intro">
  <div class="logo-anim">🛡️</div>
  <div class="game-title">PHISHGUARD</div>
  <div class="game-sub">Operación Bandeja de Entrada · v4.0</div>
  <div class="game-desc">Eres el nuevo Agente de Ciberseguridad. Analiza emails, SMS y códigos QR. Detecta el phishing antes de que comprometan la empresa. Completa misiones diarias y sube de rango.</div>
  <div class="intro-stats">
    <div class="istat"><div class="istat-v">26</div><div class="istat-l">Escenarios</div></div>
    <div class="istat"><div class="istat-v">6</div><div class="istat-l">Niveles</div></div>
    <div class="istat"><div class="istat-v">8</div><div class="istat-l">Insignias</div></div>
    <div class="istat"><div class="istat-v">3</div><div class="istat-l">Vidas</div></div>
    <div class="istat"><div class="istat-v t-glow-y">3</div><div class="istat-l">Misiones</div></div>
  </div>
  <div class="intro-missions-wrap">
    <div class="intro-missions-hdr">
      <span>📋 Misiones de hoy</span>
      <button class="btn btn-outline btn-sm" onclick="G.misiones()" style="font-size:10px;padding:5px 12px;letter-spacing:1px">VER TODAS</button>
    </div>
    <div id="intro-missions-list"></div>
    <div id="intro-xp-avail"></div>
  </div>
  <button class="btn btn-cyan btn-lg" onclick="G.start()">⚡ INICIAR MISIÓN</button>
  <div class="kb-hint">[ F ] Phishing &nbsp;|&nbsp; [ L ] Legítimo &nbsp;|&nbsp; [ Enter ] Continuar</div>
</div>

<!-- ══ MISIONES ══ -->
<div class="scr" id="s-misiones">
  <div class="ms-icon">📋</div>
  <div class="ms-title t-glow-c">MISIONES DE HOY</div>
  <div class="ms-fecha t-dim t-mono" id="ms-fecha"></div>
  <div id="ms-missions-list" style="width:100%;max-width:520px;display:flex;flex-direction:column;gap:10px"></div>
  <div id="ms-xp-total" style="margin-top:4px"></div>
  <button class="btn btn-outline btn-md" onclick="G.intro()">← VOLVER AL INICIO</button>
</div>

<!-- ══ GAME ══ -->
<div class="scr" id="s-game">
  <div class="lvl-banner" id="lvl-banner">
    <span id="b-type-icon">📧</span> Nivel <span id="b-lvl">1</span> – <span id="b-diff">Amenazas Básicas</span>
    &nbsp;|&nbsp; <span id="b-type-label">Correo</span> <span id="b-cur">1</span> de <span id="b-tot">4</span>
  </div>
  <div id="card-container" style="width:100%"></div>
</div>

<!-- ══ MODAL ══ -->
<div id="modal">
  <div class="modal-box">
    <div class="modal-hdr" id="modal-hdr">
      <div class="modal-ico" id="modal-ico"></div>
      <div><div class="modal-verd" id="modal-verd"></div><div class="modal-pts" id="modal-pts"></div></div>
    </div>
    <div class="modal-body-inner" id="modal-body"></div>
    <div class="modal-ft"><button class="btn btn-cyan btn-md" id="btn-next" onclick="G.next()">CONTINUAR →</button></div>
  </div>
</div>

<!-- ══ NIVEL SUPERADO ══ -->
<div class="scr" id="s-level">
  <div class="lc-icon" id="lc-ico">✅</div>
  <div class="lc-title t-glow-g" id="lc-title">NIVEL SUPERADO</div>
  <div class="lc-sub" id="lc-sub">NIVEL 1 – AMENAZAS BÁSICAS</div>
  <div class="lc-grid" id="lc-grid"></div>
  <div class="badge-earned" id="lc-badge" style="display:none"></div>
  <button class="btn btn-cyan btn-lg" id="btn-nextlvl" onclick="G.nextLevel()">SIGUIENTE NIVEL →</button>
</div>

<!-- ══ GAME OVER ══ -->
<div class="scr" id="s-gameover">
  <div class="go-icon">💀</div>
  <div class="go-title t-glow-r">MISIÓN FALLIDA</div>
  <div class="go-msg">Se agotaron tus vidas. El atacante logró su objetivo. En ciberseguridad real no hay segunda oportunidad.</div>
  <div class="go-score-wrap">
    <div class="go-score-lbl">Puntuación Final</div>
    <div class="go-score t-glow-c" id="go-score">0</div>
  </div>
  <div class="go-summary" id="go-summary"></div>
  <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center">
    <button class="btn btn-cyan btn-lg" onclick="G.restart()">🔄 REINTENTAR</button>
    <button class="btn btn-outline btn-md" onclick="G.intro()">🏠 INICIO</button>
  </div>
</div>

<!-- ══ VICTORIA ══ -->
<div class="scr" id="s-victory">
  <div class="vc-icon">🏆</div>
  <div class="vc-title">AGENTE ÉLITE</div>
  <div class="t-upper t-dim t-mono" style="font-size:11px;letter-spacing:5px">Misión Completada · 6/6 Niveles</div>
  <div class="vc-score-wrap">
    <div class="go-score-lbl">Puntuación Final</div>
    <div class="vc-score" id="vc-score">0</div>
  </div>
  <div id="vc-rank" class="rank-badge"></div>
  <div class="results-table" id="results-table">
    <div class="rt-head">
      <div>Nivel</div><div>Dificultad</div>
      <div style="text-align:center">✅</div>
      <div style="text-align:center">❌</div>
      <div style="text-align:center">Combo</div>
      <div style="text-align:right">Pts</div>
    </div>
    <div id="rt-rows"></div>
  </div>
  <div class="badges-gallery" id="vc-badges"></div>
  <div class="tips-box">
    <div class="tips-title">📋 Reglas de Oro – Ciberseguridad</div>
    <div class="tip"><span class="tn">01</span><span>Verifica siempre el dominio exacto del remitente antes de hacer clic en cualquier enlace.</span></div>
    <div class="tip"><span class="tn">02</span><span>Ninguna entidad legítima pide contraseña, CVV o PIN por correo electrónico. Nunca.</span></div>
    <div class="tip"><span class="tn">03</span><span>La urgencia extrema es siempre señal de alarma. Tómate 60 segundos para analizar.</span></div>
    <div class="tip"><span class="tn">04</span><span>Ante transferencias urgentes del CEO, llama directamente. El BEC es el fraude más costoso del mundo.</span></div>
    <div class="tip"><span class="tn">05</span><span>Los QR ocultan la URL destino. Verifica el remitente antes de escanear cualquier código QR corporativo.</span></div>
    <div class="tip"><span class="tn">06</span><span>Ante cualquier duda, consulta con el equipo de TI/Seguridad antes de actuar. Siempre.</span></div>
  </div>
  <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center">
    <button class="btn btn-cyan btn-lg" onclick="G.restart()">🎮 JUGAR DE NUEVO</button>
    <button class="btn btn-outline btn-md" onclick="G.intro()">🏠 INICIO</button>
  </div>
</div>
'''

JS_ENGINE = r'''
// ─── STARS BACKGROUND ────────────────────────────────────
(function(){
  const c=document.getElementById('stars-bg'),ctx=c.getContext('2d');
  let W,H,pts=[];
  function resize(){W=c.width=innerWidth;H=c.height=innerHeight;}
  function init(){pts=[];for(let i=0;i<160;i++)pts.push({x:Math.random()*W,y:Math.random()*H,r:Math.random()*1.6+.3,a:Math.random(),da:(Math.random()*.012+.003)*(Math.random()<.5?1:-1)});}
  function draw(){ctx.clearRect(0,0,W,H);pts.forEach(p=>{p.a=Math.max(0,Math.min(1,p.a+p.da));if(p.a<=0||p.a>=1)p.da*=-1;ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fillStyle=`rgba(0,229,255,${p.a*.55})`;ctx.fill();});requestAnimationFrame(draw);}
  window.addEventListener('resize',()=>{resize();init();});
  resize();init();draw();
})();

// ─── HELPERS ─────────────────────────────────────────────
const $=id=>document.getElementById(id);
const showScr=id=>{document.querySelectorAll('.scr').forEach(s=>s.classList.remove('on'));$(id).classList.add('on');};
function shuffle(arr){const a=[...arr];for(let i=a.length-1;i>0;i--){const j=0|Math.random()*(i+1);[a[i],a[j]]=[a[j],a[i]];}return a;}
function toast(msg,type='c',ms=3000){const t=document.createElement('div');t.className=`toast t${type}`;t.textContent=msg;$('toasts').appendChild(t);setTimeout(()=>{t.style.opacity='0';t.style.transition='opacity .3s';setTimeout(()=>t.remove(),300);},ms);}
function livesHTML(n){let h='';for(let i=0;i<3;i++)h+=i<n?'❤️':'🖤';return h;}
function getRank(score){let r=RANKS[0];for(const rk of RANKS)if(score>=rk.min)r=rk;return r;}

// ─── GAME ENGINE ─────────────────────────────────────────
const G=(function(){
  let st={};
  let metaState=null;
  let MISSIONS_HOY=[];
  let misionesCompletas=new Set();

  function initState(){
    st={
      score:0,lives:3,combo:0,maxCombo:0,
      correct:0,wrong:0,totalPhish:0,caughtPhish:0,missedPhish:0,falsePos:0,
      badges:new Set(),lvl:1,lvlEmails:[],lvlIdx:0,lvlStats:[],
      lvlCorrect:0,lvlWrong:0,lvlShield:true,prevLvlScore:0,
      timer:null,timeLeft:30,t0:0,answered:false,
      becCorrectos:0,quishingCorrectos:0,smishingCorrectos:0,
      respuestasRapidas:0,metaRachaActual:0,metaAciertos:0,
    };
  }
  initState();

  // ─── MISIONES ────────────────────────────────────────────
  function getMisionesKey(){const d=new Date();return `pg4_${d.getFullYear()}_${d.getMonth()+1}_${d.getDate()}`;}

  function getMisionesHoy(){
    const d=new Date();
    let seed=((d.getFullYear()*10000+(d.getMonth()+1)*100+d.getDate())|0)>>>0;
    function rng(){seed=((seed*1664525+1013904223)>>>0);return(seed/0xFFFFFFFF);}
    const pool=[...MISSIONS_POOL];const sel=[];
    while(sel.length<3&&pool.length>0){const idx=Math.floor(rng()*pool.length);sel.push(pool.splice(idx,1)[0]);}
    return sel;
  }

  function loadMisiones(){try{const r=localStorage.getItem(getMisionesKey());return new Set(r?JSON.parse(r):[]);}catch(e){return new Set();}}
  function saveMisiones(){try{localStorage.setItem(getMisionesKey(),JSON.stringify([...misionesCompletas]));}catch(e){}}

  function getMisionProgress(m){
    if(misionesCompletas.has(m.id))return{curr:m.meta,pct:100};
    let curr=0;
    switch(m.tipo){
      case 'racha':curr=Math.min(st.combo,m.meta);break;
      case 'velocidad':curr=Math.min(st.respuestasRapidas,m.meta);break;
      case 'categoria':
        if(m.cat==='BEC')curr=Math.min(st.becCorrectos,m.meta);
        else if(m.cat==='quishing')curr=Math.min(st.quishingCorrectos,m.meta);
        else if(m.cat==='smishing')curr=Math.min(st.smishingCorrectos,m.meta);
        break;
      case 'meta_racha':curr=Math.min(st.metaRachaActual,m.meta);break;
      case 'puntaje':curr=Math.min(st.score,m.meta);break;
    }
    return{curr,pct:Math.min(100,Math.round((curr/m.meta)*100))};
  }

  function checkMisiones(){
    MISSIONS_HOY.forEach(m=>{
      if(misionesCompletas.has(m.id))return;
      let done=false;
      switch(m.tipo){
        case 'racha':done=st.combo>=m.meta;break;
        case 'velocidad':done=st.respuestasRapidas>=m.meta;break;
        case 'categoria':
          if(m.cat==='BEC')done=st.becCorrectos>=m.meta;
          else if(m.cat==='quishing')done=st.quishingCorrectos>=m.meta;
          else if(m.cat==='smishing')done=st.smishingCorrectos>=m.meta;
          break;
        case 'meta_racha':done=st.metaRachaActual>=m.meta;break;
        case 'puntaje':done=st.score>=m.meta;break;
      }
      if(done){
        misionesCompletas.add(m.id);st.score+=m.xp;
        saveMisiones();hudUpdate();
        toast(`${m.emoji} Misión: ${m.titulo} +${m.xp} XP`,'y',4000);
      }
    });
  }

  function checkMisionNivelPerfecto(nivel){
    MISSIONS_HOY.forEach(m=>{
      if(misionesCompletas.has(m.id))return;
      if(m.tipo==='nivel_perfecto'&&m.nivel===nivel&&st.lvlShield){
        misionesCompletas.add(m.id);st.score+=m.xp;saveMisiones();hudUpdate();
        toast(`${m.emoji} Misión: ${m.titulo} +${m.xp} XP`,'y',4000);
      }
      if(m.tipo==='nivel_sin_vida'&&st.lvlShield&&!misionesCompletas.has(m.id)){
        misionesCompletas.add(m.id);st.score+=m.xp;saveMisiones();hudUpdate();
        toast(`${m.emoji} Misión: ${m.titulo} +${m.xp} XP`,'y',4000);
      }
    });
  }

  function updateIntroMissions(){
    const el=$('intro-missions-list');if(!el)return;
    const xpLeft=MISSIONS_HOY.reduce((s,m)=>s+(misionesCompletas.has(m.id)?0:m.xp),0);
    el.innerHTML=MISSIONS_HOY.map(m=>{
      const done=misionesCompletas.has(m.id);
      return`<div class="intro-mission-row${done?' done':''}">
        <span style="font-size:16px">${m.emoji}</span>
        <span style="flex:1;font-size:12px;color:var(--text)">${m.titulo}</span>
        <span style="font-size:11px;font-weight:700;color:${done?'var(--green)':'var(--yellow)'}">${done?'✅':'+'+m.xp+' XP'}</span>
      </div>`;
    }).join('');
    $('intro-xp-avail').textContent=xpLeft>0?`${xpLeft} XP disponibles hoy`:'¡Misiones del día completadas! 🏆';
  }

  function updateMisionesScreen(){
    const d=new Date();
    $('ms-fecha').textContent=d.toLocaleDateString('es-ES',{weekday:'long',day:'numeric',month:'long'});
    let xpLeft=0;
    $('ms-missions-list').innerHTML=MISSIONS_HOY.map(m=>{
      const done=misionesCompletas.has(m.id);
      if(!done)xpLeft+=m.xp;
      const prog=getMisionProgress(m);
      return`<div class="mission-card${done?' done':''}">
        <div class="mission-emoji">${m.emoji}</div>
        <div class="mission-info">
          <div class="mission-name">${m.titulo}</div>
          <div class="mission-desc">${m.desc}</div>
          ${!done?`<div class="mission-prog-wrap">
            <div class="mission-prog-bar"><div class="mission-prog-fill" style="width:${prog.pct}%"></div></div>
            <span class="mission-prog-text">${prog.curr}/${m.meta}</span>
          </div>`:''}
        </div>
        ${done?'<div style="font-size:22px">✅</div>':`<div class="mission-xp">+${m.xp} XP</div>`}
      </div>`;
    }).join('');
    $('ms-xp-total').textContent=xpLeft>0?`${xpLeft} XP disponibles hoy`:'¡Todas las misiones completadas! 🏆';
  }

  // ─── CARD BUILDERS ───────────────────────────────────────
  function makeQRSvg(url){
    const S=21,C=8,P=14,T=S*C+P*2;
    let seed=0;for(let i=0;i<url.length;i++)seed=(seed*31+url.charCodeAt(i))|0;
    function rng(){seed=(seed*1664525+1013904223)|0;return(seed>>>0)/0xFFFFFFFF;}
    const g=Array.from({length:S},()=>Array(S).fill(0));
    for(let r=0;r<S;r++)for(let c=0;c<S;c++)g[r][c]=rng()>.5?1:0;
    function fp(r0,c0){for(let dr=0;dr<7;dr++)for(let dc=0;dc<7;dc++){const o=dr===0||dr===6||dc===0||dc===6,i=dr>=2&&dr<=4&&dc>=2&&dc<=4;g[r0+dr][c0+dc]=(o||i)?1:0;}}
    fp(0,0);fp(0,S-7);fp(S-7,0);
    let rects='';for(let r=0;r<S;r++)for(let c=0;c<S;c++)if(g[r][c])rects+=`<rect x="${P+c*C}" y="${P+r*C}" width="${C}" height="${C}"/>`;
    return`<svg xmlns="http://www.w3.org/2000/svg" width="${T}" height="${T}" viewBox="0 0 ${T} ${T}" style="max-width:160px;border:1px solid #ddd;border-radius:4px"><rect width="${T}" height="${T}" fill="white"/><g fill="#111">${rects}</g></svg>`;
  }

  function buildEmailHTML(email){
    const type=email.type||'email';
    return`<div class="email-card">
      <div class="email-tb">
        <div class="dot" style="background:#ff5f57"></div>
        <div class="dot" style="background:#febc2e"></div>
        <div class="dot" style="background:#28c840"></div>
        <div class="tb-lbl">📥 Bandeja — ${type==='qr'?'QR':'Correo'} ${st.lvlIdx+1}/${st.lvlEmails.length} — Nivel ${st.lvl}</div>
      </div>
      <div class="email-meta">
        <div class="ef"><span class="ef-k">De:</span><span class="ef-v"><strong>${email.from_name}</strong> &lt;${email.from_email}&gt;</span></div>
        <div class="ef"><span class="ef-k">Para:</span><span class="ef-v">${email.to}</span></div>
        <div class="ef"><span class="ef-k">Fecha:</span><span class="ef-v">${email.date}</span></div>
      </div>
      <div class="email-subj">${email.subject}</div>
      <div class="email-body">${email.body_html}</div>
    </div>`;
  }

  function buildSMSHTML(email){
    const ico=email.from_name.substring(0,2).toUpperCase();
    const txt=email.body_html.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
    return`<div class="sms-frame">
      <div class="sms-topbar">
        <div class="sms-contact-ico">${ico}</div>
        <div class="sms-contact-info">
          <div class="sms-contact-name">${email.from_name}</div>
          <div class="sms-contact-num">${email.from_email}</div>
        </div>
        <span style="font-size:22px">📱</span>
      </div>
      <div class="sms-body">
        <div class="sms-date-sep">Hoy</div>
        <div class="sms-bubble-wrap">
          <div class="sms-bubble">${txt}</div>
          <div class="sms-time">9:41 AM ✓</div>
        </div>
      </div>
      <div class="sms-hint">📱 SMS — Nivel ${st.lvl} · Mensaje ${st.lvlIdx+1}/${st.lvlEmails.length}</div>
    </div>`;
  }

  function renderEmail(email){
    const type=email.type||'email';
    $('b-lvl').textContent=st.lvl;
    $('b-diff').textContent=LEVELS[String(st.lvl)].name;
    $('b-cur').textContent=st.lvlIdx+1;
    $('b-tot').textContent=st.lvlEmails.length;
    $('b-type-icon').textContent=type==='sms'?'📱':type==='qr'?'🔳':'📧';
    $('b-type-label').textContent=type==='sms'?'SMS':type==='qr'?'QR':'Correo';
    if(type==='sms'){
      $('card-container').innerHTML=buildSMSHTML(email);
    }else{
      $('card-container').innerHTML=buildEmailHTML(email);
      if(type==='qr'){
        $('card-container').querySelectorAll('.qr-placeholder').forEach(el=>{
          const url=el.getAttribute('data-url')||'https://example.com';
          const wrap=document.createElement('div');
          wrap.style.cssText='text-align:center;padding:12px 0';
          wrap.innerHTML=makeQRSvg(url);
          el.parentNode.replaceChild(wrap,el);
        });
      }
    }
  }

  // ─── METACOGNICIÓN ───────────────────────────────────────
  function showMeta(email,pts){
    metaState={email,pts};
    $('meta-q').textContent=email.meta_q;
    [0,1,2,3].forEach(i=>{
      const btn=$('meta-opt-'+i);
      $('mopt-text-'+i).textContent=email.meta_ops[i];
      btn.className='meta-option';btn.disabled=false;
    });
    $('meta-xp-msg').textContent='';
    $('meta-overlay').classList.add('on');
  }

  function evalMeta(idx){
    if(!metaState)return;
    const{email,pts}=metaState;metaState=null;
    const correct=idx===email.meta_ok;
    [0,1,2,3].forEach(i=>{
      const btn=$('meta-opt-'+i);btn.disabled=true;
      if(i===email.meta_ok)btn.classList.add('correct');
      else if(i===idx)btn.classList.add('wrong');
    });
    if(correct){
      st.score+=50;st.metaRachaActual++;st.metaAciertos++;
      $('meta-xp-msg').textContent='🧠 +50 XP — ¡Correcto! Buena metacognición.';
      hudUpdate();checkMisiones();
    }else{
      st.metaRachaActual=0;
      const keys=['A','B','C','D'];
      $('meta-xp-msg').textContent='❌ La señal clave era la opción '+keys[email.meta_ok];
    }
    setTimeout(()=>{$('meta-overlay').classList.remove('on');showModal(false,email,pts,0,1,'fail');},1600);
  }

  // ─── HUD ─────────────────────────────────────────────────
  function hudShow(on){$('hud').style.display=on?'flex':'none';}
  function barShow(on){$('action-bar').style.display=on?'flex':'none';}
  function hudUpdate(){
    $('hval-score').textContent=st.score.toLocaleString();
    $('hval-level').textContent=st.lvl;
    const m=comboMult();
    const ce=$('hval-combo');
    ce.textContent=`x${m.toFixed(1)}`;
    ce.style.color=st.combo>=5?'#ff2d55':st.combo>=3?'#ff9f0a':'#ffd60a';
    if(st.combo>0){ce.classList.remove('combo-anim');void ce.offsetWidth;ce.classList.add('combo-anim');}
    $('hval-lives').textContent=livesHTML(st.lives);
    $('hval-prog').style.width=(st.lvlIdx/Math.max(1,st.lvlEmails.length)*100)+'%';
  }
  function comboMult(){if(st.combo>=5)return 3;if(st.combo>=3)return 2;if(st.combo>=2)return 1.5;return 1;}

  // ─── TIMER ───────────────────────────────────────────────
  function timerStart(secs){
    timerStop();st.timeLeft=secs;
    $('hval-timer').textContent=secs;$('hval-timer').classList.remove('timer-warn');
    st.timer=setInterval(()=>{
      st.timeLeft--;$('hval-timer').textContent=st.timeLeft;
      if(st.timeLeft<=5)$('hval-timer').classList.add('timer-warn');
      if(st.timeLeft<=0){timerStop();if(!st.answered)timedOut();}
    },1000);
  }
  function timerStop(){clearInterval(st.timer);$('hval-timer').classList.remove('timer-warn');}
  function timedOut(){
    if(st.answered)return;st.answered=true;btnDisable();
    toast('⏰ ¡Tiempo agotado!','r');
    const email=st.lvlEmails[st.lvlIdx];
    st.wrong++;st.lvlWrong++;st.combo=0;st.lvlShield=false;
    if(email.isPhishing)st.missedPhish++;
    loseLife();hudUpdate();showModal(false,email,-100,0,1,'timeout');
  }

  // ─── LOAD EMAIL ──────────────────────────────────────────
  function emailsForLevel(lvl){return shuffle(EMAILS_RAW.filter(e=>e.level===lvl));}
  function loadEmail(){
    const email=st.lvlEmails[st.lvlIdx];
    if(!email){levelEnd();return;}
    st.answered=false;st.t0=Date.now();
    if(email.isPhishing)st.totalPhish++;
    renderEmail(email);hudUpdate();timerStart(email.time_limit);btnEnable();badgeCheck('first');
  }

  // ─── CLASSIFY ────────────────────────────────────────────
  function pick(isPhish){
    if(st.answered)return;
    st.answered=true;timerStop();btnDisable();
    const email=st.lvlEmails[st.lvlIdx];
    const ok=(isPhish===email.isPhishing);
    const timeTaken=(Date.now()-st.t0)/1000;
    const tBonus=ok?Math.round(Math.max(0,st.timeLeft)*2):0;
    const mult=comboMult();let pts=0;
    if(ok){
      pts=Math.round((email.points+tBonus)*mult);
      st.score+=pts;st.correct++;st.lvlCorrect++;st.combo++;
      st.maxCombo=Math.max(st.maxCombo,st.combo);
      if(email.isPhishing){
        st.caughtPhish++;
        const cat=email.categoria||'';
        if(cat==='BEC')st.becCorrectos++;
        if(cat==='quishing')st.quishingCorrectos++;
        if(cat==='smishing')st.smishingCorrectos++;
      }
      if(timeTaken<8)st.respuestasRapidas++;
      if(timeTaken<5)badgeCheck('speed');
      if(st.combo>=5)badgeCheck('combo5');
      hudUpdate();checkMisiones();
      showModal(true,email,pts,tBonus,mult,'ok');
    }else{
      pts=email.isPhishing?-100:-75;
      st.score=Math.max(0,st.score+pts);
      st.wrong++;st.lvlWrong++;st.combo=0;st.lvlShield=false;
      if(email.isPhishing&&!isPhish)st.missedPhish++;
      if(!email.isPhishing&&isPhish)st.falsePos++;
      loseLife();hudUpdate();
      if(email.meta_q){showMeta(email,pts);}
      else{showModal(false,email,pts,0,1,'fail');}
    }
  }

  function loseLife(){
    st.lives--;
    $('hud').style.animation='none';void $('hud').offsetWidth;
    $('hud').style.animation='hudFlash .5s ease';
    setTimeout(()=>{$('hud').style.animation='';},500);
  }

  // ─── MODAL ───────────────────────────────────────────────
  function showModal(ok,email,pts,tBonus,mult,reason){
    const isTimeout=(reason==='timeout');
    let ico,verd,ptsText,hdrBorder;
    if(isTimeout){ico='⏰';verd='TIEMPO AGOTADO';hdrBorder='rgba(255,159,10,.4)';ptsText='-100 pts · Vida perdida';}
    else if(ok){ico=email.isPhishing?'🎯':'🛡️';verd=email.isPhishing?'¡PHISHING DETECTADO!':'¡CORREO LEGÍTIMO!';
      hdrBorder='rgba(0,255,136,.35)';ptsText=`+${pts} pts (base ${email.points} + tiempo ${tBonus} x combo ${mult.toFixed(1)})`;}
    else{ico='⚠️';verd=email.isPhishing?'PHISHING NO DETECTADO':'FALSO POSITIVO';
      hdrBorder='rgba(255,45,85,.4)';ptsText=`${pts} pts · Vida perdida`;}
    $('modal-ico').textContent=ico;
    $('modal-verd').textContent=verd;
    $('modal-verd').style.color=ok&&!isTimeout?'var(--green)':'var(--red)';
    $('modal-pts').textContent=ptsText;
    $('modal-hdr').style.borderBottomColor=hdrBorder;
    let html=`<div class="modal-expl">${email.explanation}</div>`;
    if(email.isPhishing&&email.red_flags&&email.red_flags.length){
      html+=`<div class="flags-hdr">🚩 Señales de Alerta en este Correo</div>`;
      email.red_flags.forEach(f=>{html+=`<div class="flag"><div class="flag-ic">${f.icon}</div><div><div class="flag-ti">${f.title}</div><div class="flag-ds">${f.desc}</div></div></div>`;});
    }
    if(!email.isPhishing&&email.legit_reason){html+=`<div class="legit-box">✅ <strong>¿Por qué es legítimo?</strong><br>${email.legit_reason}</div>`;}
    $('modal-body').innerHTML=html;
    $('modal').classList.add('on');
  }

  function next(){
    $('modal').classList.remove('on');
    if(st.lives<=0){setTimeout(gameOver,280);return;}
    st.lvlIdx++;
    if(st.lvlIdx>=st.lvlEmails.length){setTimeout(levelEnd,280);}
    else{setTimeout(loadEmail,280);}
  }

  // ─── LEVEL END ───────────────────────────────────────────
  function levelEnd(){
    timerStop();
    const lvl=st.lvl;
    const lvlPts=st.score-st.prevLvlScore;
    st.lvlStats.push({lvl,correct:st.lvlCorrect,wrong:st.lvlWrong,combo:st.maxCombo,pts:lvlPts,total:st.lvlEmails.length});
    if(lvl===1)badgeCheck('lvl1');
    if(lvl===3)badgeCheck('lvl3');
    if(lvl===6){badgeCheck('lvl5');if(st.score>=5000)badgeCheck('elite');}
    if(st.lvlShield)badgeCheck('shield');
    checkMisionNivelPerfecto(lvl);
    hudShow(false);barShow(false);
    if(lvl===6){setTimeout(victory,280);return;}
    $('lc-ico').textContent='✅';
    $('lc-title').textContent=`NIVEL ${lvl} SUPERADO`;
    $('lc-title').className='lc-title';
    $('lc-title').style.color=LEVELS[String(lvl)].color;
    $('lc-sub').textContent=`NIVEL ${lvl} — ${LEVELS[String(lvl)].name.toUpperCase()}`;
    $('lc-grid').innerHTML=`
      <div class="lcs"><div class="lcs-v" style="color:var(--green)">${st.lvlCorrect}</div><div class="lcs-l">Aciertos</div></div>
      <div class="lcs"><div class="lcs-v" style="color:var(--red)">${st.lvlWrong}</div><div class="lcs-l">Errores</div></div>
      <div class="lcs"><div class="lcs-v" style="color:var(--cyan)">${lvlPts.toLocaleString()}</div><div class="lcs-l">Pts Nivel</div></div>
      <div class="lcs"><div class="lcs-v" style="color:var(--yellow)">x${st.maxCombo}</div><div class="lcs-l">Combo Máx.</div></div>`;
    const lb=BADGES.find(b=>b.id===[...st.badges].slice(-1)[0]);
    const lbEl=$('lc-badge');
    if(lb){lbEl.style.display='block';lbEl.innerHTML=`<div class="be-ic">${lb.ic}</div><div class="be-nm">${lb.nm}</div><div class="be-ds">${lb.ds}</div>`;}
    else{lbEl.style.display='none';}
    $('btn-nextlvl').textContent=lvl===5?'⚠️ NIVEL FINAL: Amenazas Emergentes →':'SIGUIENTE NIVEL →';
    showScr('s-level');
  }

  function nextLevel(){
    st.lvl++;st.lvlIdx=0;st.lvlCorrect=0;st.lvlWrong=0;st.lvlShield=true;
    st.prevLvlScore=st.score;st.lvlEmails=emailsForLevel(st.lvl);
    hudShow(true);barShow(true);showScr('s-game');loadEmail();hudUpdate();
    toast(`🎯 Nivel ${st.lvl} — ${LEVELS[String(st.lvl)].name}`,'c');
  }

  // ─── GAME OVER ───────────────────────────────────────────
  function gameOver(){
    timerStop();hudShow(false);barShow(false);
    $('go-score').textContent=st.score.toLocaleString();
    const pct=st.correct>0?Math.round((st.correct/(st.correct+st.wrong))*100):0;
    $('go-summary').innerHTML=`
      <div class="go-sum-row"><span class="k">Correos analizados</span><span class="v">${st.correct+st.wrong}</span></div>
      <div class="go-sum-row"><span class="k">Aciertos</span><span class="v" style="color:var(--green)">${st.correct} (${pct}%)</span></div>
      <div class="go-sum-row"><span class="k">Errores</span><span class="v" style="color:var(--red)">${st.wrong}</span></div>
      <div class="go-sum-row"><span class="k">Phishing detectado</span><span class="v">${st.caughtPhish}/${st.totalPhish}</span></div>
      <div class="go-sum-row"><span class="k">Falsos positivos</span><span class="v">${st.falsePos}</span></div>
      <div class="go-sum-row"><span class="k">Combo máximo</span><span class="v">x${st.maxCombo}</span></div>
      <div class="go-sum-row"><span class="k">Nivel alcanzado</span><span class="v">${st.lvl} / 6</span></div>`;
    showScr('s-gameover');
  }

  // ─── VICTORIA ────────────────────────────────────────────
  function victory(){
    timerStop();hudShow(false);barShow(false);
    setTimeout(()=>toast('🎉 ¡Misión completada!','g'),100);
    setTimeout(()=>toast('🏆 ¡6 niveles superados!','y'),700);
    if(st.score>=5000)setTimeout(()=>toast('💎 ¡Gran Maestro desbloqueado!','c'),1400);
    $('vc-score').textContent=st.score.toLocaleString();
    const rank=getRank(st.score);
    const rb=$('vc-rank');
    rb.textContent=`🏅 Rango: ${rank.label}`;
    rb.style.background=rank.bg;rb.style.color=rank.color;rb.style.border=`1px solid ${rank.color}40`;
    const tbody=$('rt-rows');tbody.innerHTML='';
    let totC=0,totW=0;
    st.lvlStats.forEach(s=>{
      totC+=s.correct;totW+=s.wrong;
      const row=document.createElement('div');row.className='rt-row';
      row.innerHTML=`
        <div style="font-weight:700;color:${LEVELS[String(s.lvl)].color}">Nivel ${s.lvl}</div>
        <div style="font-size:11px;color:var(--dim)">${LEVELS[String(s.lvl)].name}</div>
        <div style="text-align:center;color:var(--green);font-weight:700">${s.correct}</div>
        <div style="text-align:center;color:var(--red);font-weight:700">${s.wrong}</div>
        <div style="text-align:center;color:var(--yellow)">x${s.combo}</div>
        <div style="text-align:right;color:var(--cyan);font-weight:700;font-family:var(--mono)">${s.pts.toLocaleString()}</div>`;
      tbody.appendChild(row);
    });
    const acc=totC+totW>0?Math.round((totC/(totC+totW))*100):0;
    const total=document.createElement('div');total.className='rt-total';
    total.innerHTML=`<div style="color:var(--dim)">TOTAL</div><div style="color:var(--dim);font-size:11px">Precisión: ${acc}%</div>
      <div style="text-align:center;color:var(--green)">${totC}</div>
      <div style="text-align:center;color:var(--red)">${totW}</div>
      <div></div>
      <div style="text-align:right;color:var(--cyan);font-family:var(--mono)">${st.score.toLocaleString()}</div>`;
    tbody.appendChild(total);
    const bg=$('vc-badges');bg.innerHTML='';
    if(st.badges.size===0){bg.innerHTML='<div style="color:var(--dim);font-size:12px">Sin insignias esta partida. ¡Inténtalo de nuevo!</div>';}
    else{st.badges.forEach(id=>{const b=BADGES.find(x=>x.id===id);if(b)bg.innerHTML+=`<div class="bg-card"><span class="bi">${b.ic}</span>${b.nm}</div>`;});}
    showScr('s-victory');
  }

  // ─── BADGES ──────────────────────────────────────────────
  function badgeCheck(id){
    if(st.badges.has(id))return;st.badges.add(id);
    const b=BADGES.find(x=>x.id===id);if(!b)return;
    const el=document.createElement('div');el.className='bdg-mini';el.title=b.nm;el.textContent=b.ic;
    $('hud-badges').appendChild(el);toast(`🏅 Insignia: ${b.nm}`,'y',3500);
  }

  function btnEnable(){$('btn-phish').disabled=false;$('btn-legit').disabled=false;}
  function btnDisable(){$('btn-phish').disabled=true;$('btn-legit').disabled=true;}

  // ─── PUBLIC API ──────────────────────────────────────────
  function start(){
    initState();st.lvlEmails=emailsForLevel(1);st.prevLvlScore=0;
    hudShow(true);barShow(true);$('hud-badges').innerHTML='';hudUpdate();showScr('s-game');loadEmail();
  }
  function restart(){start();}
  function intro(){timerStop();hudShow(false);barShow(false);updateIntroMissions();showScr('s-intro');}
  function misiones(){updateMisionesScreen();showScr('s-misiones');}

  // ─── TECLADO ─────────────────────────────────────────────
  document.addEventListener('keydown',e=>{
    const k=e.key.toLowerCase();
    if($('s-game').classList.contains('on')&&!st.answered){if(k==='f')pick(true);if(k==='l')pick(false);}
    if($('modal').classList.contains('on')){if(k==='enter'||k===' ')next();}
    if($('s-level').classList.contains('on')){if(k==='enter'||k===' ')nextLevel();}
  });

  // ─── INICIALIZACIÓN ──────────────────────────────────────
  MISSIONS_HOY=getMisionesHoy();
  misionesCompletas=loadMisiones();
  updateIntroMissions();

  return{start,restart,intro,pick,next,nextLevel,evalMeta,misiones};
})();
'''

# ══════════════════════════════════════════════════════════
#  GENERADOR PRINCIPAL
# ══════════════════════════════════════════════════════════
def generate():
    # Serializar datos como JSON embebido en JavaScript
    emails_js  = json.dumps(EMAILS,        ensure_ascii=False, separators=(',', ':'))
    levels_js  = json.dumps(LEVELS,        ensure_ascii=False, separators=(',', ':'))
    badges_js  = json.dumps(BADGES,        ensure_ascii=False, separators=(',', ':'))
    ranks_js   = json.dumps(RANKS,         ensure_ascii=False, separators=(',', ':'))
    missions_js= json.dumps(MISSIONS_POOL, ensure_ascii=False, separators=(',', ':'))

    js_data = (
        f"const EMAILS_RAW={emails_js};\n"
        f"const LEVELS={levels_js};\n"
        f"const BADGES={badges_js};\n"
        f"const RANKS={ranks_js};\n"
        f"const MISSIONS_POOL={missions_js};\n"
    )

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PhishGuard v4 \u2013 Operaci\u00f3n Bandeja de Entrada</title>
<style>
{CSS}
</style>
</head>
<body>
{HTML_BODY}
<script>
{js_data}
{JS_ENGINE}
</script>
</body>
</html>"""

    output = Path('PhishGuard_v4.html')
    output.write_text(html, encoding='utf-8')
    size_kb = len(html.encode('utf-8')) // 1024
    print(f"\u2705 PhishGuard v4.0 generado correctamente")
    print(f"   Archivo : {output.resolve()}")
    print(f"   Tama\u00f1o  : {len(html):,} caracteres ({size_kb} KB)")
    print(f"   Escenarios : {len(EMAILS)} (niveles 1-6)")
    print(f"   Misiones   : {len(MISSIONS_POOL)} en pool, 3 por d\u00eda")
    print(f"\nAbre PhishGuard_v4.html en tu navegador para jugar.")

if __name__ == '__main__':
    generate()
