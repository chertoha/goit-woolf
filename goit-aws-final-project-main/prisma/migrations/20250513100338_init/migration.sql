-- CreateTable
CREATE TABLE "posts" (
    "id" SERIAL NOT NULL,
    "user" TEXT NOT NULL,
    "text" TEXT NOT NULL,

    CONSTRAINT "posts_pkey" PRIMARY KEY ("id")
);
