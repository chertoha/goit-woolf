import User from "./models/User";
import { EmailNotification } from "./services/EmailNotification";
import { Logger } from "./services/Logger";
import { NotificationService } from "./services/NotificationService";
import { PushNotification } from "./services/PushNotification";
import { SMSNotification } from "./services/SMSNotification";

const user = new User("example@email.com", "+380123456789", "device-token-abc");

const logger = new Logger();

const notificationService = new NotificationService();

notificationService.addChannel(new EmailNotification(user, logger));
notificationService.addChannel(new SMSNotification(user, logger));
notificationService.addChannel(new PushNotification(user, logger));

notificationService.send("Ваш платіж оброблено успішно!");
