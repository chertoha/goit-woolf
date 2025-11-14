import { DocumentBuilder } from "./DocumentBuilder";

const header = "ACME Corporation — Report";
const body = "Quarterly performance increased by 12%.";
const footer = "--- Confidential ---";

// const myDocument = header + "\\n\\n" + body + "\\n\\n" + footer;

// console.log(myDocument);

const builder = new DocumentBuilder();
const output = builder
  .addFooter("--- Confidential ---")
  .addHeader("ACME Corporation — Report")
  .addBody("Quarterly performance increased by 12%.")
  .build();

console.log(output);
/*
ACME Corporation — Report

Quarterly performance increased by 12%.

--- Confidential ---
*/
