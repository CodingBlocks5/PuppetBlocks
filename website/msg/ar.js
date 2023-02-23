var MSG = {
  title: "كود",
  blocks: "البلوكات",
  files: "קבצים",
  shared: "מְשׁוּתָף",
  device: "התקן",
  linkTooltip: "احفظ ووصلة إلى البلوكات.",
  runTooltip: "شغل البرنامج المعرف بواسطة البلوكات في مساحة العمل.",
  badCode: "خطأ في البرنامج:\n %1",
  timeout: "تم تجاوز الحد الأقصى لتكرارات التنفيذ .",
  trashTooltip: "تجاهل كل البلوكات.",
  catLogic: "منطق",
  catLoops: "الحلقات",
  catMath: "رياضيات",
  catText: "نص",
  catLists: "قوائم",
  catColour: "لون",
  catVariables: "متغيرات",
  catFunctions: "إجراءات",
  listVariable: "قائمة",
  textVariable: "نص",
  httpRequestError: "كانت هناك مشكلة مع هذا الطلب.",
  linkAlert: "مشاركة كود بلوكلي الخاص بك مع هذا الرابط:\n %1",
  hashError: "عذراً،ال '%1' لا تتوافق مع أي برنامج تم حفظه.",
  xmlError: "تعذر تحميل الملف المحفوظة الخاصة بك.  ربما تم إنشاؤه باستخدام إصدار مختلف من بلوكلي؟",
  badXml: "خطأ في توزيع ال \"XML\":\n %1\n\nحدد 'موافق' للتخلي عن التغييرات أو 'إلغاء الأمر' لمواصلة تحرير ال\"XML\".",
  saveTooltip: "שמור קטעי קוד לקובץ.",
  loadTooltip: "טען קטעי קוד מהקובץ.",
  notificationTooltip: "פאנל הודעות.",
  ErrorGET: "לא ניתן לטעון את הקובץ המבוקש.",
  invalidDevice: "מכשיר לא חוקי.",
  languageTooltip: "שנה שפה.",
  noToolbox: "למכשיר אין ערכת כלים.",
  networkTooltip: "התחבר דרך רשת (WebREPL, http).",
  serialTooltip: "התחבר באמצעות טורי/USB או Bluetooth (Web Serial API, https).",
  toolbarTooltip: "הצג סרגל כלים",
  wrongDevicePin: "בדוק סיכות, מכשיר היעד שונה!",
  notDefined: "לא מוגדר",
  editAsFileValue: "ערוך כקובץ",
  editAsFileTooltip: "ערוך את קוד פיתון ושמור במערכת הקבצים של המכשיר.",
  forumTooltip: "פורום עזרה.",
  accountTooltip: "הפרויקטים וההגדרות שלך.",
  blocksLoadedFromFile: "קטעי קוד נטענו מהקובץ '%1'.",
  deviceUnavailable: "מכשיר '% 1' אינו זמין.",
  notConnected: "אין חיבור לשליחת נתונים.",
  serialFroozen: "החיבור הטורי אינו מגיב.",
  notAvailableFlag: "$1 אינו זמין בדפדפן שלך.\r\nאנא ודא שדגל $1 מופעל.",

  //Blocks
  block_delay: "לְעַכֵּב",
  seconds: "שניות",
  milliseconds: "אלפיות השנייה",
  microseconds: "מיקרו שניות",
  to: "ל",
  setpin: "הגדר סיכה פלט",
  pin: "סיכה",
  read_digital_pin: "לקרוא קלט דיגיטלי",
  read_analog_pin: "לקרוא קלט אנלוגי",
  show_iot: "הצג בכרטיסיית IoT",
  data: "ערך",
  set_rtc: "להגדיר תאריך ושעה",
  get_rtc: "לקבל תאריך ושעה",
  year: "שָׁנָה",
  month: "חוֹדֶשׁ",
  day: "יְוֹם",
  hour: "שָׁעָה",
  minute: "דַקָה",
  second: "שְׁנִיָה",
  wifi_scan: "לסרוק רשתות wifi",
  wifi_connect: "להתחבר לרשת wifi",
  wifi_name: "שם רשת",
  wifi_key: "מפתח/סיסמה",
  easymqtt_start: "EasyMQTT התחל",
  easymqtt_publish: "EasyMQTT פרסם נתונים",
  topic: "נוֹשֵׂא",
  session_id: "מזהה הפעלה",
  file_open: "קובץ פתוח",
  file_name: "שם קובץ",
  file_mode: "מצב",
  file_binary: "פתוח במצב בינארי",
  file_close: "לסגור קובץ",
  file_write_line: "כתוב שורה לקובץ",
  file_line: "קַו",
  try1: "לְנַסוֹת",
  exp1: "מלבד",
  ntp_sync: "סנכרון תאריך ושעה עם NTP",
  timezone: "אזור זמן",
  project_info: "מידע על הפרויקט",
  project_info_author: "מְחַבֵּר",
  project_info_desc: "תיאור",
  easymqtt_subscribe: "EasyMQTT הירשם לנושא",
  when: "מתי",
  data_received: "מתקבל",
  easymqtt_receive: "EasyMQTT מקבל נתונים",
  relay: "ממסר",
  on: "להדליק",
  off: "לכבות",
  relay_on: "ממסר על סיכה",
  yes: "כן",
  no: "לא",
  wait_for_data: "לחכות לנתונים",
  dht_start: "הפעל את חיישן DHT",
  dht_measure: "עדכון קריאת חיישן DHT11/22",
  dht_temp: "לקבל טמפרטורה DHT11/22",
  dht_humi: "לקבל לחות DHT11/22",
  type: "סוּג",

  //Ultrasound
  hcsr_install: "התקן ספריית HCSR04",
  hcsr_init: "התחל חיישן על קולי HCSR04",
  hcsr_timeout: "זמן מקסימלי (מיקרו שנייה)",
  echo_pin: "סיכת הד",
  trigger_pin: "סיכת הדק",
  get_distance: "קרא מרחק (חיישן על קולי)",
  measure_distance: "מדד מרחק עם חיישן על קולי",

  //BMP180
  pressure: "לַחַץ",
  temperature: "טֶמפֶּרָטוּרָה",
  altitude: "גוֹבַה",
  bmp180_init: "Init BMP180",

  //SHT20
  init_sht20: "Init SHT20",
  humidity: "לחות",

  //Network
  net_http_get: "בקשת HTTP GET",
  net_http_get_status: "קוד סטטוס HTTP",
  net_http_get_content: "תוכן תגובת HTTP",
  net_http_server_start: "הפעל את שרת האינטרנט HTTP",
  net_http_server_start_port: "פורט",
  net_http_server_wait: "המתן ללקוח HTTP",
  net_http_server_requested_page: "דף אינטרנט מבוקש",
  net_http_server_send_response: "שלח תגובת HTTP",
  net_http_server_send_html: "HTML",

  // MQTT
  mqtt_init: "התחל לקוח MQTT",
  server_address: "כתובת שרת",
  server_port: "פורט שרת",
  username: "שם משתמש",
  password: "סיסמה",
  mqtt_add_to_buffer: "הוסף נתונים לתור MQTT",
  field_name: "שם שדה",
  value: "ערך",
  mqtt_publish_buffer: "שלח תור לMQTT",
  mqtt_topic: "נושא",
  qos: "QOS:",
  mqtt_most_once: "0 - עד\u00A0פעם\u00A0אחת",
  mqtt_least_once: "1 - לפחות\u00A0פעם\u00A0אחת",
  mqtt_publish_payload: "שלח נתונים לMQTT",
  payload: "נתונים",
  mqtt_subscribe: "הרשם לנושא MQTT",
  mqtt_set_callback: "MQTT הגדר פונקציה להפעלה",
  with: "עם",
  received_from: "התקבל מ",
  do: "עשה",
  mqtt_callback_tooltip: "פונקציות להפעלה חייבות להפעיל פרמטרים של נושא (topic) והודעה (msg)",
  mqtt_check_msg: "בדוק שרת MQTT להודעות ממתינות",
  mqtt_check_msg_tooltip: "בדוק אם לשרת יש הודעות ממתינות. לא בולק. הודעה תועבר לפונקציה המוגדרת",
  mqtt_wait_msg: "המתן להודעות משרת MQTT",
  mqtt_wait_msg_tooltip: "המתן להודעות שרת MQTT. פונקציה בולקת. הודעה תועבר לפונקציה המוגדרצ.",
  mqtt_disconnect: "נתק לקוח MQTT",
  mqtt_disconnect_tooltip: "נתק לקוח MQTT מהשרת.",

  //PWM
  pwm_num: "PWM #",
  frequenzy: "Frequency",
  duty_cycle: "Duty Cycle",
  pwm_num_pico: "RPi Pico PWM #",
  pwm_tooltip: "Init and set PWM with frequency (1Hz to 40MHz) and duty (0-1023)",
  pwm_freq_tooltip: "Set PWM frequency from 1Hz to 40MHz",
  pwm_duty_tooltip: "Set PWM duty range of 0-1023",
  pwm_init: "init",
  pwm_init_tooltip: "Init PWM",
  pwm_deinit: "deinit PWM #",

  //NeoPixel
  np_init: "Init NeoPixel",
  np_num_leds: "Number of LEDs",
  np_init_tooltip: "Init NeoPixel on the specified pin",
  np_controll: "Control NeoPixel",
  color: "Color",
  np_controll_tooltip: "Set NeoPixel",
  np_write: "Write NeoPixel",
  red: "Red",
  green: "Green",
  blue: "Blue",
  np_write_tooltip: "Write NeoPixel",
  np_color_tooltip_rgb: "NeoPixel LED RGB Values 0-255",
  np_color_tooltip_picker: "NeoPixel LED Picker, pick a color",
  hue: "Hue",
  saturation: "Saturation",
  lightness: "Lightness",
  np_color_tooltip_HSL: "HUE to RGB color, Hue from 0º to 360º, Saturation and Lightness from 0% to 100%.",

  //I2C Char LCD
  i2c_lcd_init: "Init I2C Character LCD Display",
  i2c_lcd_lines: "Lines",
  i2c_lcd_col: "Columns",
  i2c_lcd_clear: "Clear LCD",
  i2c_lcd_write: "Write text on LCD",
  text: "Text",
  i2c_lcd_move: "Move LCD Cursor to",
  i2c_lcd_backlight: "LCD Backlight",
  i2c_lcd_backlight_tooltip: "Set this to true/false or 1/0",
  i2c_lcd_power: "LCD Power",
  i2c_lcd_power_tooltip: "Set this to true/false or 1/0",

  //RC Servo Motor
  servo_init: "Init RC Servo Motor",
  servo_init_tooltip: "Init RC servo motor",
  servo_move: "Move Servo Motor",
  angle: "Angle",

  //Stepper Motor
  stepper_init: "Init Stepper Motor",
  stepper_step: "Stepper Step",
  steps: "Steps",

  //DC Motor
  dc_motor_init: "Init DC Motor",
  dc_motor_power: "Set DC Motor Power",
  power: "Power",
  dc_motor_dir: "Set DC Motor Direction",
  direction: "Direction",
  dc_motor_stop: "Stop DC Motor",

  //Sound
  sound_tone: "Tone (Hz)",
  sound_duration: "Duration (s):",
  sound_infinite: "(0 for infinite duration)",
  sound_tone_tooltip: "Sound - tone generator",
  sound_note: "Play music note",
  note: "Note",
  sound_note_tooltip: "Sound - tone generator (music note)",
  rtttl_play: "Play song (RTTTL)",
  song: "Song",

  //Splash screen
  splash_welcome: "Welcome to PuppetBlocks!",
  splash_footer: "Do not show this screen again",
  splash_close: "Close",
  splash_message: "<p><b>PuppetBlock</b> - open source simple visual programming language, for programming an interactive puppet, made by ESP32 micro-controller and MicroPython firmware. This platform allows text and block based programming. You can connect, program, debug and monitor using network or USB.</p><p> check our github here: <a href=https://github.com/CodingBlocks5/PuppetBlocks>https://github.com/CodingBlocks5/PuppetBlocks</a></p><p>Thank you and have fun from the PuppetBlocks Team!</p>"
};

//Toolbox categories
Blockly.Msg['CAT_TIMING'] = "תִזמוּן";
Blockly.Msg['CAT_MACHINE'] = "מְכוֹנָה";
Blockly.Msg['CAT_DISPLAYS'] = "תצוגות";
Blockly.Msg['CAT_SENSORS'] = "חיישנים";
Blockly.Msg['CAT_OUTPUTS'] = "פלטים / מפעילים";
Blockly.Msg['CAT_COMM'] = "תִקשׁוֹרֶת";
Blockly.Msg['CAT_TEMP_HUMI'] = "טמפרטורה ולחות";
Blockly.Msg['CAT_PRESS'] = "לַחַץ";
Blockly.Msg['CAT_FILES'] = "קבצים";
Blockly.Msg['CAT_NET'] = "רשת ואינטרנט";
Blockly.Msg['CAT_CONTROL'] = "לִשְׁלוֹט";
Blockly.Msg['CAT_IMU'] = "מדידת אינרציה";
Blockly.Msg['CAT_AIR'] = "איכות אוויר";
Blockly.Msg['CAT_ULTRASOUND'] = "על קולי";
Blockly.Msg['CAT_NEO'] = "NeoPixel LED Strip";
Blockly.Msg['CAT_CHAR_DISP'] = "Character display";
Blockly.Msg['CAT_RELAY'] = "Relay";
Blockly.Msg['CAT_SERVO'] = "RC Servo Motor";
Blockly.Msg['CAT_STEPPER'] = "Stepper Motor";
Blockly.Msg['CAT_DC_MOTOR'] = "DC Motor";

//Toolbox Text
Blockly.Msg['TXT_ULTRASOUND_DESCRIPTION'] = "HCSR04 ultrasound distance sensor";
Blockly.Msg['TXT_ULTRASOUND_LIB'] = "Install HCSR04 library";
Blockly.Msg['TXT_SERVO_DESCRIPTION'] = "Hobby RC Servo Motor";
Blockly.Msg['TXT_STEPPER_DESCRIPTION'] = "Stepper Motor";
Blockly.Msg['TXT_DC_MOTOR_DESCRIPTION'] = "DC Motor";
