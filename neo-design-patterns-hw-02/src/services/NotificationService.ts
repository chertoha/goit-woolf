import { INotificationChannel } from "../core/interfaces";

export class NotificationService {
  private channels: INotificationChannel[] = [];

  addChannel(channel: INotificationChannel): void {
    this.channels.push(channel);
  }

  send(message: string): void {
    this.channels.forEach((channel) => channel.send(message));
  }
}
