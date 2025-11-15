import type { FilterSection } from '../types/filter';

export const filterSections: FilterSection[] = [
  {
    title: 'Application Type',
    options: [
      { label: 'Active', count: 19, value: 'active' },
      { label: 'Archived', count: 1, value: 'archived' },
    ],
  },
  {
    title: 'Jobs',
    options: [
      {
        label: 'Digital Marketing Specialist (O26)',
        count: 8,
        value: 'job-123',
      },
      { label: 'Senior Product Designer', count: 1, value: 'job-456' },
      { label: 'Frontend Engineer (React)', count: 1, value: 'job-789' },
      { label: 'Senior Data Scientist', count: 1, value: 'job-234' },
      { label: 'UX Researcher', count: 1, value: 'job-567' },
      { label: 'Senior Backend Engineer', count: 1, value: 'job-890' },
      { label: 'Director of Marketing', count: 1, value: 'job-345' },
      { label: 'Senior DevOps Engineer', count: 1, value: 'job-678' },
    ],
  },
  {
    title: 'CRM',
    options: [
      { label: 'All Contacts', count: 20 },
      { label: 'My Contacts', count: 12 },
      { label: 'Unassigned', count: 8 },
    ],
  },
  {
    title: 'Profile Details',
    options: [
      { label: 'Has Availability', count: 6 },
      { label: 'Has Interviews', count: 5 },
      { label: 'No Availability', count: 14 },
    ],
  },
  {
    title: 'Source',
    options: [
      { label: 'LinkedIn', count: 5, value: 'LinkedIn' },
      { label: 'Referral', count: 3, value: 'Referral' },
      { label: 'Career Page', count: 2, value: 'Career Page' },
      { label: 'Indeed', count: 2, value: 'Indeed' },
      { label: 'Dribbble', count: 1, value: 'Dribbble' },
      { label: 'GitHub', count: 1, value: 'GitHub' },
      { label: 'Kaggle', count: 1, value: 'Kaggle' },
      { label: 'Stack Overflow', count: 1, value: 'Stack Overflow' },
      { label: 'Medium', count: 1, value: 'Medium' },
      { label: 'ArXiv', count: 1, value: 'ArXiv' },
      { label: 'Apple Developer', count: 1, value: 'Apple Developer' },
      { label: 'HackerOne', count: 1, value: 'HackerOne' },
    ],
  },
  {
    title: 'Responsibility',
    options: [
      { label: 'Assigned to Me', count: 12 },
      { label: 'Unassigned', count: 8 },
    ],
  },
  {
    title: 'Pipeline Tasks',
    options: [
      { label: 'Pending Tasks', count: 8 },
      { label: 'Completed Tasks', count: 12 },
      { label: 'Overdue Tasks', count: 2 },
    ],
  },
  {
    title: 'Education',
    options: [
      { label: "Bachelor's Degree", count: 12 },
      { label: "Master's Degree", count: 6 },
      { label: 'PhD', count: 2 },
    ],
  },
];
