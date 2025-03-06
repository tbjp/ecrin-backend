# Ecrin API Documentation

This document provides details about the REST API endpoints available in the Ecrin property management system backend.

## Base URL

All API endpoints are prefixed with api.

## Authentication

API requests require authentication using:

- Session authentication
- Token authentication

## Endpoints

### Properties

#### Property Management

```
GET /api/properties/
POST /api/properties/
GET /api/properties/{id}/
PUT /api/properties/{id}/
PATCH /api/properties/{id}/
DELETE /api/properties/{id}/
```

Provides CRUD operations for properties. The response includes nested staff members and issues.

**Response Fields:**

- `id`: Property identifier
- `name`: Property name
- `image`: URL to property image
- `location`: Property location
- `rooms`: Number of rooms
- `staff_count`: Number of staff members
- `bookings_count`: Number of bookings
- `has_issues`: Whether property has unresolved issues
- `issue_count`: Count of unresolved issues
- `issues`: Array of issue objects
- `staff_members`: Array of staff member objects
- `added_date`: Date when property was added

#### Issues Management

```
GET /api/issues/
POST /api/issues/
GET /api/issues/{id}/
PUT /api/issues/{id}/
PATCH /api/issues/{id}/
DELETE /api/issues/{id}/
```

Manages property issues with filtering options.

**Filter Parameters:**

- `property`: Filter by property ID
- `resolved`: Filter by resolution status (true/false)

**Response Fields:**

- `id`: Issue identifier
- `name`: Issue description
- `date_reported`: Date issue was reported
- `resolved`: Whether issue has been resolved

#### Staff Management

```
GET /api/staff/
POST /api/staff/
GET /api/staff/{id}/
PUT /api/staff/{id}/
PATCH /api/staff/{id}/
DELETE /api/staff/{id}/
```

Manages property staff members with filtering options.

**Filter Parameters:**

- `property`: Filter by property ID

**Response Fields:**

- `id`: Staff identifier
- `name`: Staff member name
- `position`: Job position
- `joined_date`: Date staff member joined

### Bookings

```
GET /api/bookings/
POST /api/bookings/
GET /api/bookings/{id}/
PUT /api/bookings/{id}/
PATCH /api/bookings/{id}/
DELETE /api/bookings/{id}/
```

Manages property bookings with filtering options.

**Filter Parameters:**

- `property`: Filter by property ID
- `status`: Filter by booking status (active/future/completed/cancelled)

**Response Fields:**

- `id`: Booking identifier
- `property`: Property ID
- `property_name`: Property name
- `guest_name`: Guest name
- `check_in`: Check-in date
- `check_out`: Check-out date
- `nights`: Number of nights (calculated)
- `price_per_night`: Price per night
- `total_price`: Total booking price
- `status`: Booking status

### Financials

#### Revenues

```
GET /api/revenues/
POST /api/revenues/
GET /api/revenues/{id}/
PUT /api/revenues/{id}/
PATCH /api/revenues/{id}/
DELETE /api/revenues/{id}/
```

Manages revenue records.

**Response Fields:**

- `id`: Revenue identifier
- `property`: Property ID
- `property_name`: Property name
- `month`: Revenue month (date)
- `month_name`: Month abbreviation
- `amount`: Revenue amount

**Additional Endpoints:**

```
GET /api/revenues/monthly_summary/?year={year}
```

Returns monthly revenue summary for a specific year (defaults to current year).

#### Expenses

```
GET /api/expenses/
POST /api/expenses/
GET /api/expenses/{id}/
PUT /api/expenses/{id}/
PATCH /api/expenses/{id}/
DELETE /api/expenses/{id}/
```

Manages expense records.

**Response Fields:**

- `id`: Expense identifier
- `property`: Property ID
- `property_name`: Property name
- `category`: Expense category
- `month`: Expense month (date)
- `month_name`: Month abbreviation
- `amount`: Expense amount
- `description`: Expense description

**Additional Endpoints:**

```
GET /api/expenses/by_category/?year={year}
```

Returns expenses grouped by category for a specific year (defaults to current year).

## Pagination

All list endpoints are paginated with 20 items per page. Use the following query parameters for pagination:

- `page`: Page number
- `page_size`: Number of items per page (optional)
