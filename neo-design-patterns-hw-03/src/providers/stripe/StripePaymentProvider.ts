import { PaymentProvider } from "../../core/PaymentProvider";

export class StripePaymentProvider implements PaymentProvider {
  authorize(amount: number): string {
    const transactionId = "stripe_" + new Date().getTime();
    console.log(`[Stripe] Authorizing $${amount}`);
    return transactionId;
  }

  capture(transactionId: string): void {
    console.log(`[Stripe] Capturing transaction ${transactionId}`);
  }

  refund(transactionId: string): void {
    console.log(`[Stripe] Refunding transaction ${transactionId}`);
  }
}
