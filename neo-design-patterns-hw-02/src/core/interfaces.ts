export interface INotificationChannel {
  send(message: string): void;
}

export interface ILogger {
  log(message: string): void;
}
