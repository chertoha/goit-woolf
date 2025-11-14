import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { LucideIcon } from "lucide-react";

interface MetricCardProps {
  title: string;
  value: number;
  icon: LucideIcon;
  variant?: "default" | "warning" | "danger";
}

export function MetricCard({
  title,
  value,
  icon: Icon,
  variant = "default",
}: MetricCardProps) {
  const getVariantStyles = () => {
    switch (variant) {
      case "warning":
        return "border-status-expiring/20 bg-status-expiring/5";
      case "danger":
        return "border-status-expired/20 bg-status-expired/5";
      default:
        return "border-primary/20 bg-primary/5";
    }
  };

  const getIconStyles = () => {
    switch (variant) {
      case "warning":
        return "text-status-expiring bg-status-expiring/10";
      case "danger":
        return "text-status-expired bg-status-expired/10";
      default:
        return "text-primary bg-primary/10";
    }
  };

  return (
    <Card className={`transition-all hover:shadow-md ${getVariantStyles()}`}>
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium text-muted-foreground">
          {title}
        </CardTitle>
        <div className={`p-2 rounded-md ${getIconStyles()}`}>
          <Icon className="h-4 w-4" />
        </div>
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold text-foreground">
          {value.toLocaleString()}
        </div>
      </CardContent>
    </Card>
  );
}
