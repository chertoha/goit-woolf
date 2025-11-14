export class AppConfigService {
  private static instance: AppConfigService;

  private constructor(
    public readonly companyName: string,
    public readonly footer: string
  ) {}

  public static getInstance(companyName: string, footer: string) {
    if (!AppConfigService.instance) {
      AppConfigService.instance = new AppConfigService(companyName, footer);
    }
    return AppConfigService.instance;
  }
}
