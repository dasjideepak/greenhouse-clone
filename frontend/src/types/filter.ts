export interface FilterOption {
  label: string;
  count?: number;
  value?: string;
}

export interface FilterSection {
  title: string;
  options: FilterOption[];
  defaultOpen?: boolean;
}
