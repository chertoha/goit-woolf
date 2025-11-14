export interface PaymentProvider {
  authorize(amount: number): string;
  capture(transactionId: string): void;
  refund(transactionId: string): void;
}
