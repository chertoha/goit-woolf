/*
  У вас є функція merge, яка поєднує два об'єкти. 
  Використовуйте generics, щоб вказати, що ці об'єкти можуть бути будь-якого типу.
*/

function merge<T, U>(objA: T, objB: U) {
  // return Object.assign(objA, objB);
  return {
    ...objA,
    ...objB,
  };
}

export {};
