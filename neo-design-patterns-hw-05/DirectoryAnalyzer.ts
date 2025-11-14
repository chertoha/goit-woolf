import * as fs from "fs";
import * as path from "path";
import { DirectoryReport } from "./DirectoryReport";

export class DirectoryAnalyzer {
  analyze(dirPath: string): DirectoryReport {
    let files = 0;
    let directories = 0;
    let totalSize = 0;
    const extensions: Record<string, number> = {};

    const traverse = (currentPath: string) => {
      const items = fs.readdirSync(currentPath, { withFileTypes: true });
      for (const item of items) {
        const itemPath = path.join(currentPath, item.name);
        if (item.isDirectory()) {
          directories++;
          traverse(itemPath);
        } else if (item.isFile()) {
          files++;
          const ext = path.extname(item.name);
          extensions[ext] = (extensions[ext] || 0) + 1;
          totalSize += fs.statSync(itemPath).size;
        }
      }
    };

    traverse(dirPath);

    return { files, directories, totalSize, extensions };
  }
}
