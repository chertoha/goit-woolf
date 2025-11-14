import * as fs from "fs/promises";
import { buildAccessLogChain } from "./chain/chains/AccessLogChain";
import { buildTransactionChain } from "./chain/chains/TransactionChain";
import { buildSystemErrorChain } from "./chain/chains/SystemErrorChain";
import { ProcessingMediator } from "./mediator/ProcessingMediator";
import { AccessLogWriter } from "./mediator/writers/AccessLogWriter";
import { TransactionWriter } from "./mediator/writers/TransactionWriter";
import { ErrorLogWriter } from "./mediator/writers/ErrorLogWriter";
import { RejectedWriter } from "./mediator/writers/RejectedWriter";
import { DataRecord } from "./models/DataRecord";

const handlerMap = {
  access_log: buildAccessLogChain,
  transaction: buildTransactionChain,
  system_error: buildSystemErrorChain,
};

async function main() {
  const raw = await fs.readFile("src/data/records.json", "utf-8");
  const records: DataRecord[] = JSON.parse(raw);
  console.log(`[INFO] Завантажено записів: ${records.length}`);

  const mediator = new ProcessingMediator(
    new AccessLogWriter(),
    new TransactionWriter(),
    new ErrorLogWriter(),
    new RejectedWriter()
  );

  for (const record of records) {
    const builder = handlerMap[record.type];
    if (!builder) {
      mediator.onRejected(record, "Unknown type");
      continue;
    }

    const handler = builder();

    try {
      const processed = handler.handle(record);
      mediator.onSuccess(processed);
    } catch (e: any) {
      mediator.onRejected(record, e.message);
    }
  }

  await mediator.finalize();
}

main();
