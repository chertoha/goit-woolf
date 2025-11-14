import { Package, AlertTriangle, XCircle, CheckCircle } from "lucide-react";
import { MetricCard } from "@/components/dashboard/MetricCard";
import { InventoryChart } from "@/components/dashboard/InventoryChart";
import { getDashboardMetrics } from "@/data/mockData";

export default function Dashboard() {
  const metrics = getDashboardMetrics();

  return (
    <div className="space-y-6">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold text-foreground">
          Medical Inventory Dashboard
        </h1>
        <p className="text-muted-foreground">
          Monitor your medical supplies and expiration dates
        </p>
      </div>

      {/* Metrics Cards */}
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <MetricCard
          title="Total Items"
          value={metrics.totalItems}
          icon={Package}
          variant="default"
        />
        <MetricCard
          title="Total Medicines"
          value={metrics.totalMedicines}
          icon={CheckCircle}
          variant="default"
        />
        <MetricCard
          title="Expiring Soon"
          value={metrics.expiringCount}
          icon={AlertTriangle}
          variant="warning"
        />
        <MetricCard
          title="Expired"
          value={metrics.expiredCount}
          icon={XCircle}
          variant="danger"
        />
      </div>

      {/* Charts */}
      <InventoryChart />
    </div>
  );
}
