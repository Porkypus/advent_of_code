import { readFileSync } from "fs";
import { join } from "path";

const path = join(__dirname, "input.txt");
const elves = readFileSync(path, "utf-8");

const res = elves
  .split("\r\n\r\n")
  .map((elf: string) => {
    return elf.split("\r\n").reduce((acc: number, curr: string) => {
      return acc + Number(curr);
    }, 0);
  })
  .sort((a: number, b: number) => b - a)
  .slice(0, 3)
  .reduce((acc: number, curr: number) => {
    return acc + curr;
  }, 0);

res;
