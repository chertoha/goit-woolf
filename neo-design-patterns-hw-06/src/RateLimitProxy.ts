import { IMessageService } from "./IMessageService";

export function createRateLimitProxy(
  service: IMessageService,
  intervalMs: number
): IMessageService {
  let lastCallTime = 0;

  return new Proxy(service, {
    get(target, prop) {
      if (prop === "send") {
        return function (this: IMessageService, ...args: [string]) {
          const now = Date.now();
          if (now - lastCallTime >= intervalMs) {
            lastCallTime = now;
            return target.send(...args);
          } else {
            console.log("[RateLimit] skipped");
          }
        };
      }

      return target[prop as keyof IMessageService];
    },
  });
}
