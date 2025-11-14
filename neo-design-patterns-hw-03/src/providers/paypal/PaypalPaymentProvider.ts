import { PaymentProvider } from "../../core/PaymentProvider";

export class PaypalPaymentProvider implements PaymentProvider {
  authorize(amount: number): string {
    const transactionId = "paypal_" + new Date().getTime();
    console.log(`[PayPal] Authorizing $${amount}`);
    return transactionId;
  }

  capture(transactionId: string): void {
    console.log(`[PayPal] Capturing transaction ${transactionId}`);
  }

  refund(transactionId: string): void {
    console.log(`[PayPal] Refunding transaction ${transactionId}`);
  }
}
