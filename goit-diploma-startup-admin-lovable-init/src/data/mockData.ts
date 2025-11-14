// Mock data for the medical inventory system

export interface StorageLocation {
  id: string;
  name: string;
  description: string;
  temperature?: string;
}

export interface Medicine {
  id: string;
  name: string;
  batchNumber: string;
  quantity: number;
  expirationDate: string;
  storageLocationId: string;
  category: string;
  supplier?: string;
  notes?: string;
}

export const mockStorageLocations: StorageLocation[] = [
  {
    id: "1",
    name: "Refrigerator Unit 1",
    description: "Main pharmaceutical refrigerator",
    temperature: "2-8°C",
  },
  {
    id: "2",
    name: "Cabinet A - Room 101",
    description: "General medicine storage cabinet",
    temperature: "Room temperature",
  },
  {
    id: "3",
    name: "Controlled Substances Safe",
    description: "Secure storage for controlled medications",
    temperature: "Room temperature",
  },
  {
    id: "4",
    name: "Emergency Kit Storage",
    description: "Emergency medication supplies",
    temperature: "Room temperature",
  },
];

export const mockMedicines: Medicine[] = [
  {
    id: "1",
    name: "Amoxicillin 500mg",
    batchNumber: "AMX-2024-001",
    quantity: 120,
    expirationDate: "2024-12-15",
    storageLocationId: "2",
    category: "Antibiotics",
  },
  {
    id: "2",
    name: "COVID-19 Vaccine",
    batchNumber: "COV-2024-089",
    quantity: 50,
    expirationDate: "2024-08-30",
    storageLocationId: "1",
    category: "Vaccines",
  },
  {
    id: "3",
    name: "Ibuprofen 400mg",
    batchNumber: "IBU-2024-045",
    quantity: 200,
    expirationDate: "2025-06-20",
    storageLocationId: "2",
    category: "Pain Relief",
  },
  {
    id: "4",
    name: "Insulin Rapid-Acting",
    batchNumber: "INS-2024-023",
    quantity: 30,
    expirationDate: "2024-09-10",
    storageLocationId: "1",
    category: "Diabetes",
  },
  {
    id: "5",
    name: "Morphine 10mg",
    batchNumber: "MOR-2024-007",
    quantity: 15,
    expirationDate: "2025-03-15",
    storageLocationId: "3",
    category: "Pain Relief",
  },
  {
    id: "6",
    name: "Aspirin 325mg",
    batchNumber: "ASP-2024-112",
    quantity: 500,
    expirationDate: "2026-01-10",
    storageLocationId: "2",
    category: "Pain Relief",
  },
  {
    id: "7",
    name: "Epinephrine Auto-Injector",
    batchNumber: "EPI-2024-033",
    quantity: 8,
    expirationDate: "2024-08-15",
    storageLocationId: "4",
    category: "Emergency",
  },
  {
    id: "8",
    name: "Ciprofloxacin 250mg",
    batchNumber: "CIP-2024-078",
    quantity: 80,
    expirationDate: "2024-11-30",
    storageLocationId: "2",
    category: "Antibiotics",
  },
  {
    id: "9",
    name: "Flu Vaccine",
    batchNumber: "FLU-2024-156",
    quantity: 100,
    expirationDate: "2025-02-28",
    storageLocationId: "1",
    category: "Vaccines",
  },
  {
    id: "10",
    name: "Acetaminophen 500mg",
    batchNumber: "ACE-2024-089",
    quantity: 300,
    expirationDate: "2024-07-25",
    storageLocationId: "2",
    category: "Pain Relief",
  },
  {
    id: "11",
    name: "Albuterol Inhaler",
    batchNumber: "ALB-2024-044",
    quantity: 25,
    expirationDate: "2025-04-18",
    storageLocationId: "2",
    category: "Respiratory",
  },
  {
    id: "12",
    name: "Nitroglycerin Tablets",
    batchNumber: "NIT-2024-022",
    quantity: 40,
    expirationDate: "2024-10-05",
    storageLocationId: "4",
    category: "Cardiac",
  },
];

// Helper functions for data analysis
export const getExpirationStatus = (
  expirationDate: string
): "expired" | "expiring" | "ok" => {
  const today = new Date();
  const expDate = new Date(expirationDate);
  const daysUntilExpiry = Math.ceil(
    (expDate.getTime() - today.getTime()) / (1000 * 60 * 60 * 24)
  );

  if (daysUntilExpiry < 0) return "expired";
  if (daysUntilExpiry <= 30) return "expiring";
  return "ok";
};

export const getStorageLocationName = (locationId: string): string => {
  const location = mockStorageLocations.find((loc) => loc.id === locationId);
  return location?.name || "Unknown Location";
};

export const getDashboardMetrics = () => {
  const totalMedicines = mockMedicines.reduce(
    (sum, med) => sum + med.quantity,
    0
  );
  const expiringCount = mockMedicines.filter(
    (med) => getExpirationStatus(med.expirationDate) === "expiring"
  ).length;
  const expiredCount = mockMedicines.filter(
    (med) => getExpirationStatus(med.expirationDate) === "expired"
  ).length;

  return {
    totalMedicines,
    totalItems: mockMedicines.length,
    expiringCount,
    expiredCount,
  };
};

export const getCategoryData = () => {
  const categories = mockMedicines.reduce((acc, medicine) => {
    acc[medicine.category] = (acc[medicine.category] || 0) + medicine.quantity;
    return acc;
  }, {} as Record<string, number>);

  return Object.entries(categories).map(([name, value]) => ({ name, value }));
};
