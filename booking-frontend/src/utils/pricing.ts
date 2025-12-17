// Helper function to generate realistic prices based on treatment category and duration
// Since prices are stored in employee_pricing table (not accessible without backend changes),
// we'll generate realistic prices based on category and duration for demo purposes

export const getTreatmentPrice = (categoryId: number, duration: number): number => {
  // Base price per minute by category
  const categoryRates: Record<number, number> = {
    1: 7,    // Hår (Hair) - 7 kr/min
    2: 6,    // Naglar (Nails) - 6 kr/min
    3: 10,   // Ansiktsbehandling (Facial) - 10 kr/min
    4: 8,    // Massage - 8 kr/min
    5: 12,   // Spa - 12 kr/min
    6: 9,    // Makeup - 9 kr/min
    7: 6,    // Vaxning (Waxing) - 6 kr/min
    8: 8,    // Skönhet (Beauty) - 8 kr/min
  };

  const ratePerMinute = categoryRates[categoryId] || 7;
  const basePrice = duration * ratePerMinute;

  // Round to nearest 50 kr for realistic pricing
  return Math.round(basePrice / 50) * 50;
};

export const formatPrice = (price: number): string => {
  return `${price} kr`;
};
