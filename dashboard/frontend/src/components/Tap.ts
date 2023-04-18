export interface Tap {
  access: string;
  address: string;
  city: string;
  description: string;
  filtration: string;
  gp_id: string;
  handicap: string;
  hours: {
    open: {
      day: number;
      time: string;
    };
    close: {
      day: number;
      time: string;
    };
  }[];
  lat: number;
  lon: number;
  norms_rules: string;
  organization: string;
  permanently_closed: boolean;
  phone: string;
  quality: string;
  service: string;
  statement: string;
  status: string;
  tap_type: string;
  tapnum: number;
  vessel: string;
  zip_code: string;
}
