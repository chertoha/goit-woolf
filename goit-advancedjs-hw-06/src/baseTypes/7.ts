/*
  Створіть функцію (isWeekend), яка приймає день тижня (з вашого enum)
  і повертає boolean значення, що вказує, чи це день робочий чи вихідний.
*/

enum WeekDays {
  MON,
  TUE,
  WED,
  THU,
  FRI,
}

enum WeekEnds {
  SAT,
  SUN,
}

type Day = WeekDays | WeekEnds;

function isWeekend(day: Day): boolean {
  return typeof day === typeof WeekEnds;
}
