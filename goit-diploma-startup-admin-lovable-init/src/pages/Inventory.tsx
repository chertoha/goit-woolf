import { useState, useMemo } from "react";
import {
  Search,
  Filter,
  Calendar,
  Package,
  MapPin,
  Plus,
  Edit,
  Trash2,
} from "lucide-react";
import { Input } from "@/components/ui/input";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
} from "@/components/ui/alert-dialog";
import { useToast } from "@/hooks/use-toast";
import {
  mockMedicines,
  mockStorageLocations,
  getExpirationStatus,
  getStorageLocationName,
  Medicine,
} from "@/data/mockData";
import { MedicineForm } from "@/components/inventory/MedicineForm";

export default function Inventory() {
  const [medicines, setMedicines] = useState<Medicine[]>(mockMedicines);
  const [searchTerm, setSearchTerm] = useState("");
  const [statusFilter, setStatusFilter] = useState<string>("all");
  const [locationFilter, setLocationFilter] = useState<string>("all");
  const [sortBy, setSortBy] = useState<string>("name");
  const [isFormOpen, setIsFormOpen] = useState(false);
  const [editingMedicine, setEditingMedicine] = useState<Medicine | null>(null);
  const [deleteDialogOpen, setDeleteDialogOpen] = useState(false);
  const [medicineToDelete, setMedicineToDelete] = useState<Medicine | null>(
    null
  );
  const { toast } = useToast();

  const filteredAndSortedMedicines = useMemo(() => {
    const filtered = medicines.filter((medicine) => {
      const matchesSearch =
        medicine.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        medicine.batchNumber.toLowerCase().includes(searchTerm.toLowerCase());

      const matchesStatus =
        statusFilter === "all" ||
        getExpirationStatus(medicine.expirationDate) === statusFilter;

      const matchesLocation =
        locationFilter === "all" ||
        medicine.storageLocationId === locationFilter;

      return matchesSearch && matchesStatus && matchesLocation;
    });

    // Sort the filtered results
    filtered.sort((a, b) => {
      switch (sortBy) {
        case "name":
          return a.name.localeCompare(b.name);
        case "expiration":
          return (
            new Date(a.expirationDate).getTime() -
            new Date(b.expirationDate).getTime()
          );
        case "quantity":
          return b.quantity - a.quantity;
        default:
          return 0;
      }
    });

    return filtered;
  }, [medicines, searchTerm, statusFilter, locationFilter, sortBy]);

  const handleAddMedicine = () => {
    setEditingMedicine(null);
    setIsFormOpen(true);
  };

  const handleEditMedicine = (medicine: Medicine) => {
    setEditingMedicine(medicine);
    setIsFormOpen(true);
  };

  const handleDeleteMedicine = (medicine: Medicine) => {
    setMedicineToDelete(medicine);
    setDeleteDialogOpen(true);
  };

  const confirmDelete = () => {
    if (medicineToDelete) {
      setMedicines((prev) => prev.filter((m) => m.id !== medicineToDelete.id));
      toast({
        title: "Medicine deleted",
        description: `${medicineToDelete.name} has been removed from inventory.`,
      });
      setMedicineToDelete(null);
      setDeleteDialogOpen(false);
    }
  };

  const handleFormSubmit = (formData: any) => {
    if (editingMedicine) {
      // Update existing medicine
      setMedicines((prev) =>
        prev.map((m) =>
          m.id === editingMedicine.id
            ? {
                ...m,
                ...formData,
                expirationDate: formData.expirationDate
                  .toISOString()
                  .split("T")[0],
              }
            : m
        )
      );
      toast({
        title: "Medicine updated",
        description: `${formData.name} has been updated successfully.`,
      });
    } else {
      // Add new medicine
      const newMedicine: Medicine = {
        id: Date.now().toString(),
        ...formData,
        expirationDate: formData.expirationDate.toISOString().split("T")[0],
      };
      setMedicines((prev) => [...prev, newMedicine]);
      toast({
        title: "Medicine added",
        description: `${formData.name} has been added to inventory.`,
      });
    }
    setIsFormOpen(false);
    setEditingMedicine(null);
  };

  const getStatusBadge = (expirationDate: string) => {
    const status = getExpirationStatus(expirationDate);
    const today = new Date();
    const expDate = new Date(expirationDate);
    const daysUntilExpiry = Math.ceil(
      (expDate.getTime() - today.getTime()) / (1000 * 60 * 60 * 24)
    );

    switch (status) {
      case "expired":
        return <Badge variant="destructive">Expired</Badge>;
      case "expiring":
        return (
          <Badge className="bg-status-expiring text-white">
            Expires in {daysUntilExpiry} days
          </Badge>
        );
      case "ok":
        return <Badge className="bg-status-ok text-white">OK</Badge>;
      default:
        return <Badge variant="secondary">Unknown</Badge>;
    }
  };

  const getRowClasses = (expirationDate: string) => {
    const status = getExpirationStatus(expirationDate);
    switch (status) {
      case "expired":
        return "border-l-4 border-l-status-expired bg-status-expired/5";
      case "expiring":
        return "border-l-4 border-l-status-expiring bg-status-expiring/5";
      case "ok":
        return "border-l-4 border-l-status-ok bg-status-ok/5";
      default:
        return "";
    }
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex justify-between items-start">
        <div>
          <h1 className="text-3xl font-bold text-foreground">
            Medicine Inventory
          </h1>
          <p className="text-muted-foreground">
            Track expiration dates and stock levels
          </p>
        </div>
        <Button onClick={handleAddMedicine} className="flex items-center gap-2">
          <Plus className="w-4 h-4" />
          Add Medicine
        </Button>
      </div>

      {/* Filters */}
      <Card>
        <CardContent className="p-4">
          <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-5">
            {/* Search */}
            <div className="relative">
              <Search className="absolute left-3 top-3 h-4 w-4 text-muted-foreground" />
              <Input
                placeholder="Search medicines..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="pl-9"
              />
            </div>

            {/* Status Filter */}
            <Select value={statusFilter} onValueChange={setStatusFilter}>
              <SelectTrigger>
                <SelectValue placeholder="Filter by status" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="all">All Status</SelectItem>
                <SelectItem value="ok">OK</SelectItem>
                <SelectItem value="expiring">Expiring Soon</SelectItem>
                <SelectItem value="expired">Expired</SelectItem>
              </SelectContent>
            </Select>

            {/* Location Filter */}
            <Select value={locationFilter} onValueChange={setLocationFilter}>
              <SelectTrigger>
                <SelectValue placeholder="Filter by location" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="all">All Locations</SelectItem>
                {mockStorageLocations.map((location) => (
                  <SelectItem key={location.id} value={location.id}>
                    {location.name}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>

            {/* Sort By */}
            <Select value={sortBy} onValueChange={setSortBy}>
              <SelectTrigger>
                <SelectValue placeholder="Sort by" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="name">Name</SelectItem>
                <SelectItem value="expiration">Expiration Date</SelectItem>
                <SelectItem value="quantity">Quantity</SelectItem>
              </SelectContent>
            </Select>

            {/* Results Count */}
            <div className="flex items-center text-sm text-muted-foreground">
              <Filter className="w-4 h-4 mr-2" />
              {filteredAndSortedMedicines.length} of {medicines.length} items
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Inventory Table */}
      <div className="space-y-2">
        {filteredAndSortedMedicines.map((medicine) => (
          <Card
            key={medicine.id}
            className={`transition-all hover:shadow-md ${getRowClasses(
              medicine.expirationDate
            )}`}
          >
            <CardContent className="p-4">
              <div className="grid gap-4 md:grid-cols-7 items-center">
                {/* Medicine Info */}
                <div className="md:col-span-2">
                  <h3 className="font-semibold text-foreground">
                    {medicine.name}
                  </h3>
                  <p className="text-sm text-muted-foreground">
                    Batch: {medicine.batchNumber}
                  </p>
                  <p className="text-xs text-muted-foreground">
                    {medicine.category}
                  </p>
                </div>

                {/* Quantity */}
                <div className="flex items-center gap-2">
                  <Package className="w-4 h-4 text-muted-foreground" />
                  <span className="font-medium">{medicine.quantity}</span>
                </div>

                {/* Expiration Date */}
                <div className="flex items-center gap-2">
                  <Calendar className="w-4 h-4 text-muted-foreground" />
                  <span className="text-sm">
                    {new Date(medicine.expirationDate).toLocaleDateString()}
                  </span>
                </div>

                {/* Storage Location */}
                <div className="flex items-center gap-2">
                  <MapPin className="w-4 h-4 text-muted-foreground" />
                  <span className="text-sm text-muted-foreground">
                    {getStorageLocationName(medicine.storageLocationId)}
                  </span>
                </div>

                {/* Status */}
                <div className="flex justify-center">
                  {getStatusBadge(medicine.expirationDate)}
                </div>

                {/* Actions */}
                <div className="flex justify-end gap-2">
                  <Button
                    variant="outline"
                    size="sm"
                    onClick={() => handleEditMedicine(medicine)}
                    className="h-8 w-8 p-0"
                  >
                    <Edit className="w-3 h-3" />
                  </Button>
                  <Button
                    variant="outline"
                    size="sm"
                    onClick={() => handleDeleteMedicine(medicine)}
                    className="h-8 w-8 p-0 text-destructive hover:text-destructive"
                  >
                    <Trash2 className="w-3 h-3" />
                  </Button>
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {filteredAndSortedMedicines.length === 0 && (
        <Card>
          <CardContent className="p-8 text-center">
            <Package className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
            <h3 className="text-lg font-semibold text-foreground mb-2">
              No medicines found
            </h3>
            <p className="text-muted-foreground">
              Try adjusting your search or filter criteria.
            </p>
          </CardContent>
        </Card>
      )}

      {/* Medicine Form Sheet */}
      <Sheet open={isFormOpen} onOpenChange={setIsFormOpen}>
        <SheetContent className="sm:max-w-[600px]">
          <SheetHeader>
            <SheetTitle>
              {editingMedicine ? "Edit Medicine" : "Add New Medicine"}
            </SheetTitle>
            <SheetDescription>
              {editingMedicine
                ? "Update the medicine information below."
                : "Enter the details for the new medicine."}
            </SheetDescription>
          </SheetHeader>
          <div className="mt-6">
            <MedicineForm
              medicine={editingMedicine || undefined}
              onSubmit={handleFormSubmit}
              onCancel={() => setIsFormOpen(false)}
            />
          </div>
        </SheetContent>
      </Sheet>

      {/* Delete Confirmation Dialog */}
      <AlertDialog open={deleteDialogOpen} onOpenChange={setDeleteDialogOpen}>
        <AlertDialogContent>
          <AlertDialogHeader>
            <AlertDialogTitle>Delete Medicine</AlertDialogTitle>
            <AlertDialogDescription>
              Are you sure you want to delete "{medicineToDelete?.name}"? This
              action cannot be undone.
            </AlertDialogDescription>
          </AlertDialogHeader>
          <AlertDialogFooter>
            <AlertDialogCancel>Cancel</AlertDialogCancel>
            <AlertDialogAction
              onClick={confirmDelete}
              className="bg-destructive text-destructive-foreground hover:bg-destructive/90"
            >
              Delete
            </AlertDialogAction>
          </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>
  );
}
