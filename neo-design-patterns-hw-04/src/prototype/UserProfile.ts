import { UserProfilePrototype } from "./UserProfilePrototype";

type Permissions = {
  canEditUsers: boolean;
  canApproveBudget: boolean;
  canAccessInternalTools: boolean;
};

type Department = "finance" | "engineering" | "marketing";

export class UserProfile implements UserProfilePrototype {
  constructor(
    public username: string,
    public department: Department,
    public permissions: Permissions
  ) {}

  //   get username(): string {
  //     return this._username;
  //   }

  //   get department(): Department {
  //     return this._department;
  //   }

  //   get permissions(): Permissions {
  //     return this._permissions;
  //   }

  //   set username(name: string) {
  //     this._username = name;
  //   }

  clone(): UserProfilePrototype {
    return new UserProfile(this.username, this.department, {
      ...this.permissions,
    });
  }
}
